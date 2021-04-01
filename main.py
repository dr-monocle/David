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
# IMPORT THE QUESTIONS AND ANSWERS LISTS LIBRARY
# ===========================================================

from lists import questions as qList
from lists import answers as aList

# ===========================================================
# DEFINE TENSORFLOW LOG LEVEL
# ===========================================================

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

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
    # if any(string in s for s in list):
    for s in list:
        if s in string:
            ans = True
            return s

    # return ''

# ===========================================================
# WELCOME SCREEN #Part 1
# ===========================================================


sleep(0.2)

print('[LOG] Getting all engines ready...')

# ===========================================================
# IMPORT NLU CLASSIFIER
# ===========================================================

from nlu.classifier import classify
from nlu.model import inputs

# ===========================================================
# WELCOME SCREEN #Part 2
# ===========================================================

speak('Getting all engines ready...')
print('[LOG] Done!')
sleep(0.3)
print('[LOG] Starting up system...')
speak('Starting up system...')
print('[LOG] Done!')
sleep(0.3)
print('[LOG] Setting up your preferences...')
speak('Setting up your preferences...')
print('[LOG] Done!')
sleep(0.3)

print("""
 ____                 _      _ 
|  _ \   __ _ __   __(_)  __| |
| | | | / _` |\ \ / /| | / _` |
| |_| || (_| | \ V / | || (_| |
|____/  \__,_|  \_/  |_| \__,_|
""")
sleep(0.3)
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

    text = search(text, inputs)

    if text == None:
        entity = None
    else:
        entity = classify(text)

    # 1. Get Time

    if entity == 'time\\getTime':

        spkList = SystemInfo.get_time()

        spkHr = str(spkList[0])
        spkMin = str(spkList[1])

        if len(spkHr) == 2:
            strHr = spkHr
        else:
            strHr = '0' + spkHr

        if len(spkMin) == 2:
            strMin = spkMin
        else:
            strMin = '0' + spkMin

        if strHr == '00' and strMin == '00':
            spkHr = 'midnight'
            spkMin = ''
        elif strHr == '12' and strMin == '00':
            strHrL = ['midday', 'noon', '12']
            spkHr = rdm.choice(strHrL)
            if strHr == '12':
                spkMin = 'o\'clock'
            else:
                spkMin = ''
        elif (strMin == '00' and strHr != '00') or (strMin == '00' and strHr != '12'):
            spkMin = 'o\'clock'

        timeChoiceP = rdm.choice(aList.timePL)
        timeChoiceS = rdm.choice(aList.timeSL)

        prt = timeChoiceP + f'{strHr}:{strMin}.'
        if strMin == 'o\'clock':
            spkStr = timeChoiceS + spkHr + ' ' + spkMin + '.'
        elif strMin == '':
            spkStr = timeChoiceS + spkHr + '.'
        else:
            spkStr = timeChoiceS + spkHr + ' ' + spkMin + '.'

        print(prt)
        speak(spkStr)

    elif entity == 'time\\getDate':
        dateL = SystemInfo.get_date()

        day = str(dateL[0])
        month = str(dateL[1])
        year = str(dateL[2])

        if len(day) == 2:
            strDay = day
        else:
            strDay = '0' + day
        
        if len(month) == 2:
            strMonth = month
        else:
            strMonth = '0' + month

        # Day to speak
        if len(day) == 1:
            if day == '1':
                day = '1st'
            elif day == '2':
                day = '2nd'
            elif day == '3':
                day = '3rd'
            else:
                day = day + 'th'
        elif len(day) == 2:
            if day[1] == '1' and day != '11':
                day = day + 'st'
            elif day[1] == '2' and day != '12':
                day = day +'nd'
            elif day[1] == '3' and day != '13':
                day = day + 'rd'
            else:
                day = day + 'th'

        # Month to speak
        month = aList.monthL[int(month)]

        dateChoiceS = rdm.choice(aList.dateSL)
        dateChoiceP = rdm.choice(aList.datePL)

        strSpk = dateChoiceS + 'the ' + day + ' of ' + month + ' of the year of ' + year + '.'
        strPrt = dateChoiceP + strDay + '/' + strMonth + '/' + year + '.'

        print(strPrt)
        speak(strSpk)