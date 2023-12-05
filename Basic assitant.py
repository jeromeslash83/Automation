import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import sys

def listen_to_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            speak("Sorry, I did not understand that.")
            return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def perform_task(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f'The time is {current_time}')

    elif 'open' in command and 'website' in command:
        speak('Which website should I open?')
        site = listen_to_command()
        if site:
            webbrowser.open(site)
            speak('Opening website')

    elif 'open' in command and 'folder' in command:
        speak('Which folder do you want to open?')
        folder = listen_to_command()
        if folder:
            if sys.platform == 'win32':
                os.startfile(folder)
            else:
                speak("Folder opening is not supported on this operating system.")
            speak('Opening folder')

# Main loop
while True:
    speak('What can I do for you?')
    command = listen_to_command()
    if command:
        perform_task(command)
    speak('Do you want to continue?')
    if listen_to_command() == 'no':
        break
