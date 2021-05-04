from speak_your_voice import speak
import psutil
import platform
from datetime import datetime


def sys_info():
    print('===='+"System Information"+'====')
    speak('here is your system information')

    uname = platform.uname()
    print(f"System: {uname.system}")
    speak(f"System: leenux")
    print(f"Node Name: {uname.node}")
    speak(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    speak(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    speak(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    speak(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    speak(f"Processor: {uname.processor}")




