import ctypes
import os
import subprocess
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyjokes
import playsound
import psutil
import pyautogui
import editables
import datetime



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def cpu():
    usage = str(psutil.cpu_percent())
    speak(f'Your system is Using {usage}% of CPU')

def battery():
    battery = psutil.sensors_battery()
    battery = battery.percent
    speak(f'Your system has {str(battery)}% of battery')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")

    speak("Iam Layla ! your personal virtual assistant ! Iam Online and ready ! please let me know, how can i help you ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogninsing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        speak("Could you repeat again...")
        return "None"
    return query

def screenshot():
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().strftime("%H-%M-%S")

    image = pyautogui.grab()
    speak('showing the screen shot')
    image.show()
    image.save(str(date) + '-' + str(time) + '.png')

    speak('Screenshot saved successfully')
    
  


def start():
    query = takeCommand().lower()

    if "greet" in query or "greet me" in query or "wish me" in query or "wish" in query:
        speak("on your way , sir !")
        wishMe()

    elif "wikipedia" in query:
        speak("Searching Wikipedia .....")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif "open youtube" in query:
        speak("Opening Youtube")
        webbrowser.open("youtube.com")

    elif "open stackoverflow" in query:
        speak("Opening stackoverflow")
        webbrowser.open("stackoverflow.com")

    elif "open google" in query:
        speak("Opening google")
        webbrowser.open("google.com")

    elif 'the time' in query:
        st = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {st}")

    # elif "open code" in query:
    #     codepath =

    elif 'how are you' in query:
        speak("I am fine, Thank you")
        print("I am fine, Thank you")
        speak("How are you Sir?")
        print("How are you Sir?")

    elif "what's your name" in query or "what is your name" in query:
        speak("My friends call me Layla !")
        # speak("Do you like it sir?")

    elif "who is your owner" in query or "who is your boss" in query or "who made you" in query or "who created you" in query:
        speak("I have been created and programmed for perfoming daily utilities and tasks that are provided by my Boss , Mr. Narsimha")

    elif "narasimha" in query or "narsimha" in query:
        speak("He is my Boss ! and iam his lovely assistant , Layla!")

    elif "will you be my gf" in query or "will you be my bf" in query:
        speak("I'm not sure about, may be you should give me some time")

    elif "how are you" in query:
        speak("I'm fine, glad you me that")

    elif "i love you" in query:
        speak("It's hard to understand but i accept it in a positive manner")

    elif 'lock device' in query or "lock my device" in query or 'lock the device' in query:
        speak("locking the device ! Be patient")
        ctypes.windll.user32.LockWorkStation()

    elif 'restart' in query or 'restart the pc' in query or 'restart the system' in query or 'system restart' in query:
        speak("Your System is restarting now...")
        os.system("shutdown /r /t 1")

    elif 'shutdown system' in query or 'shutdown the system' in query or 'shutdown device' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        os.system("shutdown /s /t 1")
    
    elif 'display cpu usage' in query or 'cpu usage' in query:
        cpu()

    elif 'display battery percentage' in query or 'battery' in query:
        battery()

    elif 'take a screenshot' in query or 'screenshot' in query:
        screenshot()

    elif 'joke' in query:
        speak(pyjokes.get_joke())

    elif "favourite song of mine" in query or "favourite song of narsimha" in query or "favourite song" in query:
        speak("Playing my Master's favourite song...")
        webbrowser.open("C:\\Users\\pc\\Desktop\\Projects\\VA\Habibi song.mp3")

    elif "what is my name" in query:
        speak("Narsimha")

    elif 'exit' in query:
        speak("Thanks for giving me your time")
        exit()


if __name__ == "__main__":
    # while True:
    while True:
        start()
