"""
Details Finder
By: ADWAITH.A
Instagrame: av_movi_tozz
Website: https://kiteav.blogspot.com/
"""
import pyjokes
import tkinter as tk
import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import cv2

import pyautogui
import openai
openai.api_key=""
root = tk.Tk()
root.title("")
root.geometry('90x40')

root.configure(bg='blue')  # Change 'blue' to your desired color

listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', 'english+f2')
engine.say('ഹലോ, നിങ്ങൾക്ക് സുഖമാണോ')
engine.runAndWait() 

def on_enter(event):
    button.config(text="Hovering!")

def on_leave(event):
    button.config(text="Click Me!")

def chat_with_gpt(prompt):
    response= openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content": prompt}]
    )
    return response.choices[0].message.content.strip()

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
            if 'mummu'   in command:
                command=command.replace('mummu', '')
            
                
    except:
        
        print('not listening')
        pass
    return command

def run_ammu():
    command=take_command()
    if 'play' in command:
        song=command.replace('play',"")
        if 'song' in command:
            song=command.replace('song',"")
            print(command)
            talk('playing'+ song)
            pywhatkit.playonyt(song)
        if 'vedio' in command:
            song=command.replace('vedio',"")
            print(command)
            talk('playing'+ song)
            pywhatkit.playonyt(song)
    elif "your"  in command:
        name=command.replace("your","")
        if "name" in command:
            name=name.replace("name","")
            print('ammu')
            talk('my name is ammu')
        elif "mothers" in command:
            name=name.replace("mothers","")
            if "name" in command:
                print('shari')
                talk('my mothers name is shari')
        elif "mother's" in command:
            name=name.replace("mother","")
            if "name" in command:
                print('shari')
                talk('my mothers name is shari')
        elif "fathers" in command:
            name=name.replace("fathers","")
            if "name" in command:
                print('amalraj')
                talk('my fathers name is amalraj')
        elif "father's" in command:
            name=name.replace("father's","")
            if "name" in command:
                print('amalraj')
                talk('my fathers name is amalraj')
        elif "father" in command:
            name=name.replace("father","")
            if "name" in command:
                print('amalraj')
                talk('my fathers name is amalraj')
    elif 'time' in command:
        if 'railway' in command:
            print(command)
            time=datetime.datetime.now().strftime('%I:%M')
            talk('the time is'+ time)
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
    elif 'joke' in command:
        jock=pyjokes.get_joke()
    elif "add" in command :
        if __name__ == "__main__": 
            response=chat_with_gpt(command)
            print("chat bot" , response)
            talk(response)    
    elif "multipli" in command :
        if __name__ == "__main__": 
            response=chat_with_gpt(command)
            print("chat bot" , response)
            talk(response)
    elif "divid" in command :
        if __name__ == "__main__": 
            response=chat_with_gpt(command)
            print("chat bot" , response)
            talk(response)
    elif "add" in command :
        if __name__ == "__main__": 
            response=chat_with_gpt(command)
            print("chat bot" , response)
            talk(response)
    else:
        if __name__ == "__main__": 
            response=chat_with_gpt(command)
            print("chat bot" , response)
            talk(response)
def button_click():
    tk.Button(root,
                    text="stat")
    while True:   
          run_ammu()
def on_enter(event):
    button.config(text="Speak!")

def on_leave(event):
    button.config(text="Ammu")
button = tk.Button(root,
                   border=0,
                   highlightthickness=0,
                    text="Ammu",
                      command=button_click,
                        bg="blue", fg="white",
                          activebackground="green",
                            activeforeground="white",
                              padx=200,
                                pady=100
                                )
button.pack(pady=0)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
root.mainloop()
