
import boto3
import json
import boto3.ec2
import sys
import boto3.session

##https://stackoverflow.com/questions/42809096/difference-between-resource-client-and-session/42818143#42818143
##https://stackoverflow.com/questions/42809096/difference-between-resource-client-and-session/42818143
myregion = 'us-east-1'


##session = boto.Session()
session = boto3.session.Session(profile_name="rivigo")
ssm_resource = session.client('ssm')
print(ssm_resource)
