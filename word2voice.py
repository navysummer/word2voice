import sys
major = sys.version_info.major
if major == 2:
    import pyttsx
elif major == 3:
    import pyttsx3 as pyttsx
else:
    raise Exception('current python version is not supported')
words = "你好"
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-15)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume)
engine.say(words)
engine.runAndWait()