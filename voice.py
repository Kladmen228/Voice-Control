import speech_recognition as sr
import pyttsx3
import sys
import os
rec = sr.Recognizer() #


def speak(phrase):
    voice = pyttsx3.init()
    voice.say(phrase)
    voice.runAndWait()


def listeningToCommand():
    with sr.Microphone() as mic:
        print("говорите")
        rec.pause_threshold = 1 # ожидание команды
        rec.adjust_for_ambient_noise(mic, duration=1) # чтобы шумов было меньше
        audio = rec.listen(mic)
    try:
        command = rec.recognize_google(audio).lower()
        speak("команда " + command + " принята")
    except sr.UnknownValueError:
        command = listeningToCommand()
    return command


def performance(command):
    if 'hello' in command:
        speak("hello")
    elif '' in command:
        pass    # тут можно делать любую дичь 
    elif '' in command:
        pass    # тут можно делать любую дичь
    elif 'стоп' in command or 'stop' in command:
        sys.exit()


speak("я родился")
while True:
    performance(listeningToCommand())
