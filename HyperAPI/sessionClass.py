import sys
import os
import requests
import jwt
import urllib3

from os.path import join
from requests_toolbelt.multipart.encoder import MultipartEncoder, MultipartEncoderMonitor

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Session:
    """Session to HyperCube Server."""

    def __init__(self, username, password, url=None, token=None):
        """
        Initiate a session with hypercube rest api (using username, password, url).

        and defines:
        - self.session,
        - self.api_entry_point
        """
        self.url = url or os.environ.get('H3_API_URI') or 'https://localhost:3000/app'
        self.data_folder = ''
        self.is_local = False

        # Initiate session parameters
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers = {
            "Content-Type": 'application/json;charset=UTF-8',
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
            "Accept-Language": "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",
            "Connection": "keep-alive",
        }

        # api entry point: base url
        self.api_entry_point = '{}/api/v1/'.format(self.url)

        self.__login(username, password, token)

    def __login(self, username=None, password=None, token=None):
        api_token = token or os.environ.get("API_TOKEN")
        if (not username or not password) and api_token is not None:
            auth_data = {'apiToken': api_token, 'api': True}
        else:
            if not username or not password:
                raise ValueError('You must specify url AND username AND password')
            auth_data = {'username': username, 'password': password}

        # Connect to server with authentication
        resp = self.session.post('{}/{}'.format(self.url, 'auth/login'), json=auth_data)
        if not resp.ok:
            raise requests.exceptions.HTTPError(
                'Impossible to authenticate to: {}. Reason is {}'.format('{}/{}'.format(self.url, 'auth/login'),
                                                                         resp.reason))

        # Retrieve jwt token
        jwt_token = resp.json()
        if not jwt_token:
            raise requests.exceptions.HTTPError('Authentication response does not contain a jwt token')

        try:
            decoded_jwt = jwt.decode(jwt_token, verify=False)
        except jwt.InvalidTokenError:
            raise requests.exceptions.HTTPError('Authentication response does not contain a valid jwt token')

        self.user__id = decoded_jwt.get('_id', None)
        if not self.user__id:
            raise requests.exceptions.HTTPError('Authentication response does not contain _id')

        # Set jwt token in session headers
        self.session.headers['Authorization'] = 'Bearer {}'.format(jwt_token)

    def refresh(self, username=None, password=None, token=None):
        self.__login(username, password, token)

    def request(self, method, url, params=None, json=None, data=None, affinity=None, streaming=False):
        """Make a request to rest API and return response as json."""
        params = params or {}
        json = json or {}
        data = data or {}
        if self.api_entry_point.endswith('/') and url.startswith('/'):
            url = '{}{}'.format(self.api_entry_point, url[1:])
        else:
            url = '{}{}'.format(self.api_entry_point, url)
        method = method.upper()
        if method not in ['GET', 'POST']:
            raise ValueError("method should be in ['GET', 'POST']")

        headers = self.session.headers.copy()
        if affinity is not None:
            headers['HC-WorkerAffinity'] = affinity

        if method == 'POST' and streaming:
            # Create new data with encoder
            encoder = MultipartEncoder(fields=data)

            multi_data = MultipartEncoderMonitor(encoder, None)

            headers['Content-Type'] = multi_data.content_type
            resp = self.session.request(method, url, params=params, json=json, data=multi_data, headers=headers)
        else:
            resp = self.session.request(method, url, params=params, json=json, data=data, headers=headers)

        if not resp.ok:
            raise requests.exceptions.HTTPError(
                'Error while trying to do a {} at {}. Reason is {}\nResponse content: {}'.format(method, url,
                                                                                                 resp.reason,
                                                                                                 resp.text),
                response=resp.status_code,
                request=url)
        try:
            return resp.json()
        except Exception:
            return resp.content

    def request_v2(self, method, url, params=None, json=None, data=None, affinity=None, streaming=False):
        """Make a request to rest API and return response."""
        params = params or {}
        json = json or {}
        data = data or {}
        url = '{}{}'.format(self.api_entry_point, url)
        method = method.upper()
        if method not in ['GET', 'POST']:
            raise ValueError("method should be in ['GET', 'POST']")

        headers = self.session.headers.copy()
        if affinity is not None:
            headers['HC-WorkerAffinity'] = affinity

        if method == 'POST' and streaming:
            # Create new data with encoder
            encoder = MultipartEncoder(fields=data)

            def callback(monitor):
                if 'size' in data:
                    msg = '{0:.0f}% uploaded '.format(100 * monitor.bytes_read / int(data['size']))
                else:
                    msg = '{} bytes uploaded '.format(monitor.bytes_read)
                print(msg, flush=True, end='\r')

            multi_data = MultipartEncoderMonitor(encoder, callback)

            headers = self.session.headers.copy()
            headers['Content-Type'] = multi_data.content_type
            resp = self.session.request(method, url, params=params, json=json, data=multi_data, headers=headers)
        else:
            resp = self.session.request(method, url, params=params, json=json, data=data, headers=headers)

        try:
            return resp
        except Exception:
            print("Unexpected error")
            sys.exit()

    def get(self, url, params=None, json=None, data=None):
        return self.request('GET', url, params, json, data)

    def post(self, url, params=None, json=None, data=None, streaming=False):
        return self.request('POST', url, params, json, data, streaming)
