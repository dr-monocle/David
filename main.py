# ===========================================================
# IMPORT LIBRARIES
# ===========================================================

from vosk import Model, KaldiRecognizer, SetLogLevel
import datetime
import os
import pyaudio
import pyttsx3
import json
from time import sleep
import random as rdm

# ===========================================================
# IMPORT THE CORE LIBRARY
# ===========================================================

from core import SystemInfo

# ===========================================================
# IMPORT NLU CLASSIFIER
# ===========================================================

from nlu.classifier import classify

# ===========================================================
# IMPORT THE QUESTIONS AND ANSWERS LISTS LIBRARY
# ===========================================================

from lists import questions as qList
from lists import answers as aList


# ===========================================================
# OUTPUT FUNCTION CONFIGURATION
# ===========================================================

eng = pyttsx3.init()


def speak(text):
    eng.say(text)
    eng.runAndWait()

# ===========================================================
# INPUT FUNCTION CONFIGURATION
# ===========================================================

SetLogLevel(-1)

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                input=True, frames_per_buffer=8000)
stream.start_stream()

def listen():
    data = stream.read(16000)
    if len(data) == 0:
        return ''
    if rec.AcceptWaveform(data):
        # Result is a str
        res = rec.Result()
        # Convert result to dict/json
        res = json.loads(res)
        # Taking only what user said
        text = res['text']
        
        return text

# ===========================================================
# SEARCH FUNCTION CONFIGURATION
# ===========================================================

def search(string, list):
    if string == None:
        string = 'aqwrterhs'
    ans = False
    #if any(string in s for s in list):
    for s in list:
        if s in string:
            ans = True
            return ans

    # return ans

# ===========================================================
# WELCOME SCREEN
# ===========================================================

sleep(0.1)

print('[LOG] Getting all engines ready...')
speak('Getting all engines ready...')
print('[LOG] Done!')
sleep(0.5)
print('[LOG] Starting up system...')
speak('Starting up system...')
print('[LOG] Done!')
sleep(0.5)
print('[LOG] Setting up your preferences...')
speak('Setting up your preferences...')
print('[LOG] Done!')
sleep(0.5)

print("""
 ____                 _      _ 
|  _ \   __ _ __   __(_)  __| |
| | | | / _` |\ \ / /| | / _` |
| |_| || (_| | \ V / | || (_| |
|____/  \__,_|  \_/  |_| \__,_|
""")
sleep(0.5)
speak('I am ready now!')
print('Hello, I\'m David, your AI Virtual Assistant!')
speak('Hello! Ready to work?')

# ===========================================================
#  CODE
# ===========================================================

while True:
    
    text = listen()

    if text == '':
        choice = rdm.choice(aList.errorL)
        print(choice)
        speak(choice)

        break

    # ========================================================
    # AI FUNCTIONALITIES
    # ========================================================

    # 1. Tell Time
    
    if search(text, qList.time):

    #if text == None:
    #    text = 'aqwrterhs'

    #    if any(qList.time) in text:
        if len(str(SystemInfo.get_time()[0])) == 2:
            strHr = str(SystemInfo.get_time()[0])
        else:
            strHr = '0' + str(SystemInfo.get_time()[0])

        if len(str(SystemInfo.get_time()[1])) == 2:
            strMin = str(SystemInfo.get_time()[1])
        else:
            strMin = '0' + str(SystemInfo.get_time()[1])

        timeChoiceP = rdm.choice(aList.timePL)
        timeChoiceS = rdm.choice(aList.timeSL)

        prt = timeChoiceP + f'{strHr}:{strMin}.'
        spkHr = str(SystemInfo.get_time()[0])
        spkMin = str(SystemInfo.get_time()[1])
        print(prt)
        speak(timeChoiceS + spkHr +
                ' hours and ' + spkMin + ' minutes.')

    # Shutdown System

    elif search(text, qList.exit):
        print('Are you sure that you want to close David?')
        speak('Are you sure that you want to close David?')

        op = listen()

        while op != None:

            if op in 'yesyeahyapyayahyha':
                print('Shutting down...')
                speak('I will wait for the next time! Goodbye!')
                exit()
            
            else: 
                break


