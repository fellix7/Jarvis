import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import pywhatkit as kit
import smtplib
import eye_controlled_mouse

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("Welcome Mr. Tanwar. I am Jarvis, your AI assistant, waiting for your orders... ")
    speak("Welcome Mr. Tanwar. I am Jarvis, your AI assistant, waiting for your orders... ")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:   

        print("Couldn't understand what you said. Please try saying that again...")
        speak("Couldn't understand what you said. Please try saying that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "search google" in query:
            speak("Searching Google...")
            query = query.replace("Google", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to google")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Opening Google...")
            webbrowser.open("google.com")        

        elif "open stackoverflow" in query:
            speak("Opening Stackoverflow...")
            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in query:
            music_dir = "C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(music_dir,)
            speak('opening spotify')

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open vs code" in query:
            speak("opening VS code")
            code_path = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'send message' in query:
            try:
                to = '+91 '
                speak("What should I send?")
                content = takeCommand()
                speak("To whom should I send?")
                to += takeCommand()
                kit.sendwhatmsg(to,content, datetime.datetime.now().hour, ((datetime.datetime.now().minute)+1))
                speak("Message has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able send the message.")

        elif 'control the screen using my eyes' in query:
            speak("Now you can use your eyes to control the screen.")
