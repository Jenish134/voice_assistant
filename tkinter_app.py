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
from tkinter import *


def start1():
    speak_your_voice.speak('speak anything')
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

    if 'todo' in speak1:
        todo()
    if 'to do' in speak1:
        todo()

    if 'translate' in speak1:
        translate_api.translate_def()

    if 'weather' in speak1:
        weather_report.main()

    if 'tell me ' in speak1:
        qs = speak1
        web_acrapping.web_scraping(qs)





BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

    # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50",
                               fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06,
                             rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        """ msg2 = f"{bot_name}: {start1(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED) """

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
