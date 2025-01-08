#!/usr/bin/env python
# coding: utf-8

# # Date : 8/1/25

# In[3]:


#Installing libraries
get_ipython().system('pip install SpeechRecognition pyttsx3 pyaudio')


# # Creating a virtual assistant

# In[ ]:


import pyttsx3
engine = pyttsx3.init()
def speak(text):
    """Make the assistant speak"""
    engine.say(text)
    engine.runAndWait()
def main():
    speak("Hello! I am your simple bot friend.")
    
    while True:
        command = input("You: ").lower()
        if "hello" in command:
            speak("Hi there! Welcome to Mallareddy University.")
        elif "what's your name" in command or "what is your name" in command:
            speak("My name is Simplpe ot from Mallareddy University.")
        elif "goodbye" in command:
            speak("Goodbye! Have a great day at Mallareddy University.")
            break
        else:
            speak("I didn't understand thyat. Please try again.")
if __name__ == "__main__":
    main()


# # Using Scikit learn

# In[2]:


#predicting future values
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
years = [[2015],[2016], [2017], [2018], [2019], [2020]]
values = [200, 220, 240, 260, 280, 300]
years_train, years_test, values_train, values_test = train_test_split(years, values, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(years_train, values_train)
future_year = [[2025]]
predicted_value = model.predict(future_year)
print(f"Predicted value for the year {future_year[0][0]}: {predicted_value[0]:.2f}")


# In[ ]:




