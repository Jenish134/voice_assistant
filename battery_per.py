# python script showing battery details
import psutil
import speak_your_voice

# function returning time in hh:mm:ss
def convertTime(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	return "%d:%02d:%02d" % (hours, minutes, seconds)

def battery_show():


    # returns a tuple
    battery = psutil.sensors_battery()
    p=int(battery.percent)
    # converting seconds to hh:mm:ss
    t=convertTime(battery.secsleft)
    T=convertTime(battery.secsleft)

    if battery.power_plugged == False:
        print(f'your battery is in not charging mode.Your battery percentage is {p}% and remaning time to use it is {t}. ')
        speak_your_voice.speak(f'your battery is in not charging mode.Your battery percentage is {p}% and remaning time to use it is {t}. ')
    else:
        print(f'your battery is in charging mode.Your battery percentage is {p}%.')
        speak_your_voice.speak(f'your battery is in charging mode.Your battery percentage is {p}%.')

    


