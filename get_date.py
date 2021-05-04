import datetime
from speak_your_voice import speak

def date():

    e = datetime.datetime.now()

    print ("Today's date is %s/%s/%s" % (e.day, e.month, e.year))
    speak("Today's date is %s/%s/%s" % (e.day, e.month, e.year))

