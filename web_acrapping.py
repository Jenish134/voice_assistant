# speak function chalu karvanu baki che

import speak_your_voice
from threading import Thread
import requests
from bs4 import BeautifulSoup



def web_scraping(qs):
    
    URL = 'https://www.google.com/search?q=' + qs
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    links = soup.findAll("a")
    all_links = []
    for link in links:
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            all_links.append(
                (link.get('href').split("?q=")[1].split("&sa=U")[0]))

    flag = False
    for link in all_links:
        if 'https://en.wikipedia.org/wiki/' in link:
            wiki = link
            flag = True
            break

    div1 = soup.find_all("div", class_="Ap5OSd")
    div2 = soup.find_all("div", class_="nGphre")

    if len(div1) != 0:
        answer = div1[0].text+"\n"+div1[0].find_next_sibling("div").text
        # print(answer)
        #speak_your_voice.speak(answer)
        print(div1[0].find_next_sibling("div").text)
    elif len(div2) != 0:
        answer = div2[0].find_next("span").text+"\n" + \
            div2[0].find_next("div", class_="kCrYT").text
        print(answer)
        speak_your_voice.speak(answer)
        # print(div2[0].find_next("div",class_="kCrYT").text)
    elif flag == True:
        page2 = requests.get(wiki)
        soup = BeautifulSoup(page2.text, 'html.parser')

        title = soup.select("#firstHeading")[0].text
        print(title)
        paragraphs = soup.select("p")
        for para in paragraphs:
            if bool(para.text.strip()):
                answer = title + "\n" + para.text
                # print(answer)
                # speak(answer)
                break
        # print(paragraphs)
        # just grab the text up to contents as stated in question
        intro = '\n'.join([para.text for para in paragraphs[0:2]])
        print(intro)
        speak_your_voice.speak(intro)
    else:
        print("Not Found")
        #engine.say("Not Found")
        # engine.runAndWait()

    
    
