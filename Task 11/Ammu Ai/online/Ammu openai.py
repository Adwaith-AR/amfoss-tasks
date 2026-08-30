import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import openai
openai.api_key=""

listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', 'english+f2')
engine.say('i am ammu ')
engine.runAndWait() 

#engine.say('tell me darling')
def chat_with_gpt(prompt):
    response= openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content": prompt}]
    )
    return response.choices[0].message.content.strip()
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
            if 'ammu' in command:
                command=command.replace('ammu', '')
            else:
                command= 0
                
    except:
        pass
    return command
def run_ammu():
    command=take_command()
    if "your" and "name" in command:
        name=command.replace("your","")
        name=name.replace("name","")
        print('ammu')
        talk('my name is'+ 'ammu')
    if "quit"in command:
        quit()
    elif __name__ == "__main__": 
        response=chat_with_gpt(command)
        print("chat bot" , response)
        talk(response)
    
while True:   
    run_ammu()
