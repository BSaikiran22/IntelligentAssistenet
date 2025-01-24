from gemini import gemin
# from assi import assistant
import speech_recognition as sr
import time
import requests
import json
# import pyttsx3
from news import speak_news

import pygame

from gtts import gTTS


import os 

language = 'en'
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# print("sdfghjkl")



def speak(audio):
    myobj = gTTS(text=audio, lang=language, slow=False)

    myobj.save("welcome.mp3")

    pygame.mixer.init()
    try:
        pygame.mixer.music.load("welcome.mp3")
        pygame.mixer.music.play()
        
        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        print('Playing sound using pygame.mixer')
    except Exception as e:
        print(f"Error playing sound: {e}")
    finally:
        pygame.mixer.quit()  # Clean up pygame mixer



    # engine.say(audio)
    # engine.runAndWait()


r=sr.Recognizer()
def callgem():
    with sr.Microphone() as source:
        # speak("please say something")
            a=r.listen(source)
            print("you said  : "+r.recognize_google(a,language ='en-us'))
            k=r.recognize_google(a,language ='en-us')
            print(k)
        #     speak(k)
        #     k=k+"in 5 senetences"
            if "news" in k:
                speak_news() 
            else:
                response = gemin(k)
                print(response)
                speak(response)

# callgem()