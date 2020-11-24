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


    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("\nsay something (im giving up on you)")
            audio = r.listen(source, timeout=5, phrase_time_limit=3)

        print("done recording. recognizing...")
        return(r.recognize_google(audio, language="fr-FR"))
    except:
        print("Message non reconnu")
        return "erreur"


def test():
    msg = ""
    while True:
        while msg != "a":
            msg = input(
                "Entrer a pour lancer une reconnaissance de voix, quit pour quitter\n")
            if msg == "quit":
                sys.exit(0)
        output = record_and_recognize()
        print("output: {}".format(output))
        msg = ""


def return_sentence():
    msg = ""
    output = ""
    while msg != "ok":
        print("Initialisation...")
        output = record_and_recognize()
        print("output: {}".format(output))
        msg = input(
            "Entrer ok pour retourner ce message, ou autre chose pour réessayer\n")
    return output


# test()
