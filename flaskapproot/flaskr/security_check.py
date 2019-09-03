import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger.info("I am in security_check")
class User():


    def __init__(self,id,name,password):

        self.id = id
        self.username = name
        self.password = password

    def __str__(self):
        return f"User ID: {self.id}"


users = [ User(1,'hello','pass'),
          User(2,'h@h.com','password')]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    logger.info("password:"+ password)
    if user and password == user.password:
        return user

def identity(payload):
    logger.info(str(payload))
    user_id = payload['identity']
    return userid_table.get(user_id, None)
