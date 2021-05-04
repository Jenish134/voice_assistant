import datetime
from speak_your_voice import speak

def time():

    e = datetime.datetime.now()

    print ("The time is now ",e.strftime("%I:%M:%S %p"))
    speak("the time is now " + e.strftime("%I:%M:%S %p"))

