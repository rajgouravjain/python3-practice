import boto3
import boto3.session
session = boto3.session.Session(profile_name="devops")
##session = boto.Session()
s3_resource = session.resource('s3')
for bucket in s3_resource.buckets.all():
    print(bucket.name)

