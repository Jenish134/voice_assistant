from translate import Translator
import speak_your_voice

def translate_def():
    
    print('speak what language you are gonna using.')
    speak_your_voice.speak('speak what language you are gonna using.')
    A = speak_your_voice.get_audio()
    origin_lan = A

    print('speak in which language you wanna translate..')
    speak_your_voice.speak('speak in which language you wanna translate..')
    B = speak_your_voice.get_audio()
    translation_lan = B

    print('speak here your text you wanna translate.')
    speak_your_voice.speak('speak here your text you wanna translate.')
    C = speak_your_voice.get_audio()
    sentance = C

    translator= Translator(from_lang=origin_lan,to_lang=translation_lan)
    translation = translator.translate(sentance)
    print(translation)
    speak_your_voice.speak(translation)
