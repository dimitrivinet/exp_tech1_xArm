import speech_recognition as sr
import pyaudio
import time 

r = sr.Recognizer()

mic = sr.Microphone()

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