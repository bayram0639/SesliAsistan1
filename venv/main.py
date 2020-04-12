import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio,language='tr-TR')
        except sr.UnknownValueError:
            speak('Anlayamadım')
        except sr.RequestError:
            speak('Sistem çalışmıyor')
        return voice

def response(voice):
    if 'Merhaba Tulpar' in voice:
        speak('Merhaba Bayram')
    if 'Nasılsın?' in voice:
        speak('İyi senden')    
    if 'Saat kaç?' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))   
    if 'Arama yap' in voice:
        search = record('Ne aramak istiyorsun?')   
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
    if 'Kapat' in voice:
        speak('Görüşürüz')                                
        exit()