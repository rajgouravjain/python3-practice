class Alerts(object):
    def __init__(self,file):
        self.file = file

    def _dispatch(self,msg):
        with  open(file,'w') as f:
            f.write(msg)

    def send(self,msg):
        _dispatch(msg)

class EmailAlerts(Alerts):

    def __init__(self):
        super().__init__()

    def _dispatch(self):


