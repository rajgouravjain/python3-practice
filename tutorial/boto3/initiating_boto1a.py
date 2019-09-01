
import boto3
import json
import boto3.ec2
import sys
import boto3.session

##https://stackoverflow.com/questions/42809096/difference-between-resource-client-and-session/42818143#42818143
##https://stackoverflow.com/questions/42809096/difference-between-resource-client-and-session/42818143
myregion = 'us-east-1'


##session = boto.Session()
session = boto3.session.Session(profile_name="devops")
ec2_resource = session.resource('ec2')
ec2_client  = ec2_resource.meta.client
#print ec2_client.describe_instances()

response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'zoom*',
            ]
        },
    ],
    DryRun=False
)
print response
