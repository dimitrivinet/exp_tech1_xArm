#!/usr/bin/env python3

import speech_recognition as sr
import pyaudio
import time 
import sys


def record_and_recognize():
    r = sr.Recognizer()

    mic = sr.Microphone()
    print(mic)

    # print(sr.Microphone.list_microphone_names())

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("say something (im giving up on you)")
        audio = r.listen(source)

    print("done recording. recognizing...")
    try:
        print("output:  {}".format(r.recognize_google(audio, language="fr-FR")))
    except:
        print("Message non reconnu")

msg = ""
while True:
    while msg != "a":
        msg = input("Entrer a pour lancer une reconnaissance de voix, quit pour quitter\n")
        if msg == "quit":
            sys.exit(0)
    record_and_recognize()
    msg = ""