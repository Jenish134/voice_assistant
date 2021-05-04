import requests
from pprint import pprint
import speak_your_voice


def weather_data(query):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?' +
                       query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
    return res.json()


def print_weather(result, city):
    print("{}'s temperature: {}°C ".format(city, result['main']['temp']))
    speak_your_voice.speak("{}'s temperature: {}°C ".format(city, result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    speak_your_voice.speak("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    speak_your_voice.speak("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
    speak_your_voice.speak("Weather: {}".format(result['weather'][0]['main']))


def main():
    #get city name 
    print('speak your city here')
    speak_your_voice.speak('speak your city here')
    A = speak_your_voice.get_audio()
    city = A
    print()
    try:
        query = 'q='+city
        w_data = weather_data(query)
        speak_your_voice.speak(print_weather(w_data, city))
    except:
        return 
