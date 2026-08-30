import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', 'english+m2')
engine.say('ammu is for assistance what can i do for you')

#engine.say('tell me darling')

engine.runAndWait()
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
            if 'ammu'   in command:
                command=command.replace('ammu', '')
            
                
    except:
        pass
    return command
def run_ammu():
    command=take_command()
    if 'play' in command:
        song=command.replace('play',"")
        print(command)
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif "your" and "name" in command:
        name=command.replace("your","")
        name=name.replace("name","")
        print('ammu')
        talk('my name is'+ 'ammu')
    elif 'time' in command:
        if 'railway' in command:
            print(command)
            time=datetime.datetime.now().strftime('%I:%M')
        else:
            print(command)
            time=datetime.datetime.now().strftime('%I:%M %p')
        talk('the time is'+ time)
    elif 'what is' in command:
        search=command.replace('what is',"")
        print(command)
        results=wikipedia.summary(search, 1)
        print (results)
        talk(results)
    elif 'who is' in command:
        search=command.replace('who is',"")
        print(command)
        results=wikipedia.summary(search, 1)
        print (results)
        talk(results)
    elif 'tell me about' in command:
        search=command.replace('tell me about',"")
        print(command)
        results=wikipedia.summary(search, 1)
        print (results)
        talk(results)
    else:
        print(command)

while True:   
    run_ammu()