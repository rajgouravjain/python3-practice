import fire


__author = "Rajgourav Jain"

class IngestionStage(object):
  def __init__(self,ing):
    self.ing = ing

  def run(self):
    return 'Ingesting! Nom nom nom... {}'.format(self.ing)

class DigestionStage(object):
  def __init__(self,ong):
     self.ong = ong
  def run(self, volume=1):
    return ' '.join(['Burp!'] * volume) + ' {}'.format(self.ong)

  def status(self):
    return 'Satiated.'

class Pipeline(object):

  def __init__(self,ping="",pong=""):
    self.ingestion = IngestionStage(ping)
    self.digestion = DigestionStage(pong)

  def run(self):
      irun = self.ingestion.run()
      drun = self.digestion.run(volume=5)
      dstatus = self.digestion.status()
      return " ".join([irun,drun,dstatus])
 
if __name__ == '__main__':
  fire.Fire(Pipeline)
