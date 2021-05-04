from covid import Covid
import speak_your_voice

def covid_tracking(country_name):
    covid = Covid()
    country_Name = covid.get_status_by_country_name(country_name)

    data ={
        key:country_Name[key]
        for key in country_Name.keys() and {'confirmed',
                                    'active',
                                    'deaths',
                                    'recovered'}
    }
    print('here is your covid data')
    speak_your_voice.speak('here is your covid data')
    print(data)