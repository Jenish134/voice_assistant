# import the time module
from speak_your_voice import speak
import time


# define the countdown func.
def countdown(t):
	
	speak('your timer starts now')

	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1

	print("ok it's over")
	speak('ok its over')
	
