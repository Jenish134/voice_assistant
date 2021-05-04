from os import stat_result
from web_browser import google1
import speak_your_voice
import battery_per
import covid_tracker
import create_html_css_js
import get_date
import get_news
import mail_sender
import send_wpmsg
import stock_nifty
import system_information
import tic_toe
import get_time
import timer
import todo

import translate_api
import weather_report
import web_acrapping
import web_browser


def start1():
    speak_your_voice.speak('speak anything')
    print('speak anything .......')
    speak2 = speak_your_voice.get_audio()
    speak1 = speak2.lower()

    if 'google' in speak1:
        lst = [speak1]

        def convert(lst):
            return ([i for item in lst for i in item.split()])
        X = convert(lst)
        qs = ' '.join(X[1::])
        web_browser.google1(qs)
    
    if 'stock' in speak1:
        stock_nifty.nifty()

    if 'battery percentage' in speak1:
        battery_per.battery_show()
    
    if 'covid' in speak1:
        print('tell me your country')
        speak_your_voice.speak('tell me your country')
        country_name = speak_your_voice.get_audio()
        covid_tracker.covid_tracking(country_name)

    if 'create web file' in speak1:
        speak_your_voice.speak('tell me your project name')
        project_name = speak_your_voice.get_audio()
        print(project_name)
        create_html_css_js.create_file(project_name)

    if 'date' in speak1:
        get_date.date()
    
    if 'give me news' in speak1:
        get_news.NewsFromBBC()

    if 'give me time' in speak1:
        get_time.time()

    if 'system information' in speak1:
        system_information.sys_info()

    if 'play tik' in speak1:
        game_instance =  tic_toe.Tic_Tac_Toe()
        game_instance.mainloop()

    if 'timer' in speak1:
        speak_your_voice.speak('tell me how many sec you want for your timer')
        X2 = speak_your_voice.get_audio()
        t = int(X2)
        timer.countdown(t) 

    if 'translate' in speak1:
        translate_api.translate_def()

    if 'weather' in speak1:
        weather_report.main()

    if 'tell me ' in speak1:
        qs = speak1
        web_acrapping.web_scraping(qs)


    if 'send mail' in speak1:
        mail_sender.mail_sender1()


while True:
    start1()