from fabric import Connection
from fabric.group import ThreadingGroup
from fabric.exceptions import GroupException
from fabric.config import Config

from invoke import task
import boto3 

config = Config(user_ssh_path="/Users/rajgouravj/.ssh/oregon_config")
@task(iterable=["tag_key","tag_value"])
def execute(c,tag_key,tag_value,**kwargs):
  for key,value in kwargs.items():
    print(key,value)
  target_hosts=[]
  client =  boto3.client("ec2")
  response = client.describe_instances(
    Filters=[
        {
            'Name': "tag:" + tag_key,
            'Values': [tag_value]
            },
        {
            'Name': "instance-state-name",
            'Values': ["running"]
            }
    
       ]
  )
  for r in response['Reservations']:
      for i in r["Instances"]:
        target_hosts.append(i["PrivateIpAddress"])
  print(target_hosts)
  conn = ThreadingGroup(*target_hosts,config=config)
  print(conn)
  run(conn,"ls -al")
def run(c,command):
  try:
    r=c.run(command, hide=True, warn=True)
  except GroupException as e:
    print("Error running command " + command + " on server with exception message " + str(e))
