import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
 # Use the first voice available

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ammu' in command:
                command = command.replace('ammu', '')
            return command
    except Exception as e:
        print(f"Error: {e}")
        return ""

def run_ammu():
    command = take_command()
    if not command:
        return

    if 'play' in command:
        song = command.replace('play', "")
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'your name' in command:
        talk('my name is ammu')
    elif 'time' in command:
        time_format = '%I:%M %p' if 'railway' not in command else '%H:%M'
        current_time = datetime.datetime.now().strftime(time_format)
        talk('the time is ' + current_time)
    elif 'what is' in command:
        search = command.replace('what is', "")
        results = wikipedia.summary(search, 1)
        talk(results)
    elif 'who is' in command:
        search = command.replace('who is', "")
        results = wikipedia.summary(search, 1)
        talk(results)
    elif 'tell me about' in command:
        search = command.replace('tell me about', "")
        results = wikipedia.summary(search, 1)
        talk(results)
    else:
        talk("I didn't understand that command. Please try again.")

while True:
    run_ammu()
