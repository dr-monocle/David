##############################
#      IMPORT LIBRARIES      #
##############################

import speech_recognition as sr
import datetime

##############################
#    INPUT CONFIGURATION     #
##############################

r = sr.Recognizer()

# Get the default microphone
with sr.Microphone() as source:
    # Listen to a command, using AVD
    while True:
        audio = r.listen(source)
        # Recognizes speech using Google as a service: online
        google = r.recognize_google(audio)
        sphinx = r.recognize_sphinx(audio)

        print(f'Google: [{google}]\nSphinxs: [{sphinx}]')
