from typing import List
import speak_your_voice

QS = speak_your_voice.get_audio()

lst = [QS]

def convert(lst):
	return ([i for item in lst for i in item.split()])

X = convert(lst)	




P = ' '.join(X[1::])


print(P)