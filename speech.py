import speech_recognition as sr
import re

r = sr.Recognizer() 

with sr.Microphone() as source:
    print('Speak Now!')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text = re.sub('\'','',text)
        print('You said :',text)
        f = open("Speech.txt", "w")
        f.write(text)
        f.close()
    except:
        print('Fail to RECOGNITION')

