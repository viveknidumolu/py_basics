#!/usr/bin/env python
# coding: utf-8

# # adding voice command to chat bot

# In[ ]:


import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
def speak(text):
    """Make the assistant speak"""
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening, please speak.")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
            return ""
def main():
    speak("Hello! I am your simple bot friend.")
    
    while True:
        command = listen()
        if "hello" in command:
            speak("Hi there! Welcome to Mallareddy University.")
        elif "what's your name" in command or "what is your name" in command:
            speak("My name is Simplpe ot from Mallareddy University.")
        elif "goodbye" in command:
            speak("Goodbye! Have a great day at Mallareddy University.")
            break
        else:
            speak("I didn't understand that. Please try again.")
if __name__ == "__main__":
    main()


# In[1]:


get_ipython().system('pip install pyttsx3')

