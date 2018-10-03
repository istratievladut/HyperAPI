class TimeOutSettings(object):
    """Manages timeout settings for different work states:
        - pending : work has not yet started and is waiting for resources
        - starting : resources have been allocated and the work is being launched
        - progress : work is active and computing"""

    def __init__(self, pending=3600, starting=300, progress=3600):
        self._pending = pending
        self._starting = starting
        self._progress = progress

    def __repr__(self):
        return "<{}>({}) - pending:{} | starting:{} | in progress:{}".format(self.__class__.__name__,
                                                                             id(self),
                                                                             self._pending,
                                                                             self._starting,
                                                                             self._progress)

    def __str__(self):
        _msg = self.__doc__
        _msg += '\nCurrent values:'
        _msg += '\n\t- Pending     : {}s'.format(self._pending)
        _msg += '\n\t- Starting    : {}s'.format(self._starting)
        _msg += '\n\t- In Progress : {}s'.format(self._progress)
        return _msg

    def get_pending_timeout(self):
        """
        Get the timeout value for 'pending' status
        :param name (str): The name of the dataset
        :return: timeout value in seconds (int/float)
        """
        return self._pending

    def get_starting_timeout(self):
        """
        Get the timeout value for 'starting' status
        :return: timeout value in seconds (int/float)
        """
        return self._starting

    def get_progress_timeout(self):
        """
        Get the timeout value for 'in progress' status
        :return: timeout value in seconds (int/float)
        """
        return self._progress

    def set_pending_timeout(self, value):
        """
        Set the timeout value for 'pending' status
        :param value (str/int/float): The timeout new value
        """
        self._pending = float(value)

    def set_starting_timeout(self, value):
        """
        Set the timeout value for 'starting' status
        :param value (str/int/float): The timeout new value
        """
        self._starting = float(value)

    def set_progress_timeout(self, value):
        """
        Set the timeout value for 'in progress' status
        :param value (str/int/float): The timeout new value
        """
        self._progress = float(value)
