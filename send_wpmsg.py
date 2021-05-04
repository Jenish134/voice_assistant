import pywhatkit


def send_msg():

    mo_no = input('Enter your mobile no with the country code with plus sign :- ')
    
    sending_msg = input("Enter msg you wanna give youy entered mo number :- ")

    hour1 = int(input("enter your hour timing when you wanna send msg in 24 hr formate. :- "))

    minute1 = int(input('Enter minuit for your entered hour. :- '))

    pywhatkit.sendwhatmsg(mo_no,sending_msg,hour1,minute1)

