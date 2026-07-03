import subprocess
import os
import speech_recognition as sr
import pyttsx3
import datetime

#Set up text to speech
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id) # 0 for male 1 for female

#Converting text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Function to record the user speech
def record_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Recording started")
        audio = r.listen(source)
        print("Recording finished.")
    
    try:
        text = r.recognize_google(audio)
        if text.strip() == "":
            print("No speech dectected try again")
            return record_speech()
        return text
    except sr.UnknownValueError:
        print("Unable to recognize speech")
        return record_speech()
    except sr.RequestError as e:
        print("Error ocurred during speech recognition:", str(e))
        return record_speech()
 
#Time Function to get time
def time():
    time = datetime.datetime.now().strftime("%H:%M:%S") 
    speak(time)
    print(time)   

#Function to greet user
def wishes():
    speak("welcome back sir")

    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good morning")
    elif hour>12 and hour<=18:
        speak("Good afternoon")
    elif hour>18 and hour<=24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("How can i help you today")

#Functions to opens apps
def open_app(app_name):
    app_paths = {
    "google": r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "game": r"C:\Users\Matt\Downloads\GTA San Andreas\gta_sa.exe",
    "visual studio code": r"C:\Users\Matt\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    }

    app_name = app_name.lower()
    if app_name in app_paths:
        app_path = app_paths[app_name]
        if os.path.exists(app_path):
            speak(f"Opening {app_name}")
            subprocess.Popen([app_path])
        else:
            speak(f"{app_name} not found on this system.")
    else:
        speak("No app found.")

#Function to do smonething


# Main loop
if __name__ == "__main__":
    wishes()
    while True:
        prompt = record_speech().lower()
        print(prompt)
        if "goodbye" in prompt:
            speak("Goodbye sir")
            break 
        elif "time" in prompt:
            time()
        elif prompt.startswith(("start", "open")):
            app_name = prompt.replace("open", "").replace("start", "").strip()
            open_app(app_name)
        else:
            print('Do not know what to do')
            speak('Do not know what to do')