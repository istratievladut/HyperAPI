import subprocess
import os
import json
import time
import argparse
from os.path import join as j

FNULL = open(os.devnull, 'w')


class AwsDeployer():

    def __init__(self, path, bucket, region):
        if not os.path.isdir(path):
            raise Exception("path " + str(path) + " is not a folder")
        self.path = path
        self.bucket = bucket
        self.region = region
        self.get_prefix()

    def get_prefix(self):
        if os.path.isdir(self.path):
            self.prefix = self.path.split('/')
        self.prefix = self.prefix[len(self.prefix) - 1]

    def deploy_all(self):
        print("deploying " + self.prefix + "...", end="")
        path = self.path
        print(path)
        proc = subprocess.Popen("aws s3 sync " + path + " s3://" + self.bucket + "/" + self.prefix +
                                " --region " + self.region,
                                shell=True, stdout=FNULL)
        code = proc.wait()
        if code == 0:
            print(" ok.")
        else:
            print(" error.")
            raise Exception("Error when pushing prefix " + self.prefix)

    def get_bucket_policies(self):
        print("get bucket policies")
        proc = subprocess.Popen("aws s3api get-bucket-policy --bucket " + self.bucket +
                                " --region " + self.region + " --query Policy --output text > policy.json ",
                                shell=True, stdout=FNULL)
        code = proc.wait()
        if code != 0:
            print("No bucket policies found, creating an empty one.")
            data = {
                "Statement": [
                    {
                        "Effect": "Allow", "Principal": "*", "Action": "s3:GetObject", "Resource": f"arn:aws:s3:::{self.bucket}/index.html"
                    }
                ]
            }
            with open("policy.json", "w+") as f:
                f.write(json.dumps(data))
                f.close()
            print("policy file created")

    def push_bucket_policies(self):
        print("push bucket policies")
        proc = subprocess.Popen("aws s3api put-bucket-policy --bucket " + self.bucket +
                                " --region " + self.region + " --policy file://policy.json",
                                shell=True, stdout=FNULL)
        code = proc.wait()
        if code != 0:
            raise Exception("Error when pushing policies")

    def update_local_policies(self):
        print("update policies")
        with open("policy.json", "r") as f:
            policy = json.load(f)
        current_ressources = []
        try:
            for statement in policy["Statement"]:
                current_ressources.append(statement["Resource"])
        except:
            raise Exception("Wrong policy format")
        string_prefix = "arn:aws:s3:::" + self.bucket + "/" + self.prefix + "/*"
        if string_prefix not in current_ressources:
            policy["Statement"].append({
                'Effect': 'Allow',
                'Action': 's3:GetObject',
                'Sid': 'PublicReadForGetBucketObjects',
                'Principal': '*',
                'Resource': string_prefix
            })
        with open("policy.json", "w") as f:
            json.dump(policy, f)

    def update_policies(self):
        print("update all policies")
        self.get_bucket_policies()
        self.update_local_policies()
        self.push_bucket_policies()


if __name__ == '__main__':
    t0 = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', required=True,
                        help='build folder path - path to the folder containing the doc to deploy')
    parser.add_argument('-b', '--bucket', required=False, default="hyperapi-doc",
                        help='bucket s3 to deploy the doc in')
    parser.add_argument('-r', '--region', required=False, default="eu-west-3",
                        help='region of the bucket s3 to deploy the doc in')

    args = parser.parse_args()

    awsDeployer = AwsDeployer(args.path, args.bucket, args.region)
    t1 = time.time()
    print()
    print("---------------------------------")
    print("-----------deploy all------------")
    print("---------------------------------")
    awsDeployer.deploy_all()
    t2 = time.time()
    print("completed in " + str(t2 - t1)[0:5] + "s.")

    print()
    print("---------------------------------")
    print("------Updates policies-----------")
    print("---------------------------------")
    awsDeployer.update_policies()
    t3 = time.time()
    print("completed in " + str(t3 - t2)[0:5] + "s.")
    print("\n\n\n")
    print("Deployement stage completed in " + str(t3 - t0)[0:5] + "s.")
