import sys
major = sys.version_info.major
if major == 2:
    import pyttsx
elif major == 3:
    import pyttsx3 as pyttsx
else:
    raise Exception('current python version is not supported')

class Voice(object):
    """docstring for Voice"""
    def __init__(self, words=''):
        super(Voice, self).__init__()
        self.words = words
        self.engine = pyttsx.init()

    def start(self,words,rate=200,volume=1.0):
        self.words = words
        if self.engine.isBusy():
            # rate = self.engine.getProperty('rate')
            # print(rate)
            self.engine.setProperty('rate', rate-15)
            # volume = self.engine.getProperty('volume')
            # print(volume)
            self.engine.setProperty('volume', volume)
            self.engine.say(self.words)
            self.engine.runAndWait()

    def stop(self):
        if self.engine.isBusy():
            self.engine.stop()