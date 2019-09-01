import sys
import boto3

##https://stackoverflow.com/questions/42809096/difference-between-resource-client-and-session/42818143#42818143


## Creating your own session
#####################################
#session = boto3.session.Session()
#s3_client = session.client('s3')
#s3_resource = session.resource('s3')
#
###################################
#import boto3
#client = boto3.client(
#    's3',
#    aws_access_key_id=ACCESS_KEY,
#    aws_secret_access_key=SECRET_KEY,
#    aws_session_token=SESSION_TOKEN,
#)

# Or via the Session
#session = boto3.Session(
#    aws_access_key_id=ACCESS_KEY,
#    aws_secret_access_key=SECRET_KEY,
#    aws_session_token=SESSION_TOKEN,
#)

#################################
#session = boto3.Session(profile_name='dev')
# Any clients created from this session will use credentials
# from the [dev] section of ~/.aws/credentials.
#_dev_s3_client = session.client('s3')

ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
print(response)