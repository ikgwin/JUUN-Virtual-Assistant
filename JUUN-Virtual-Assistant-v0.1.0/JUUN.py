# importing the speech recognition library that is able to listen to the users microphone and register what the user is saying
from http import client
from re import L
import urllib.request
import speech_recognition as sr

# importing pyttsx3 which basically onverts text to speech
import pyttsx3

# importing webbrowser which opens web broswers in another window in the users default browser
import webbrowser as wb

# importing urllib in order to open browsers when user asks to search something or open a website
import urllib3
opera_path = "C:\\Users\\isaak\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
wb.register('opera', None, wb.BackgroundBrowser(opera_path))

#importing datetime which allows us to manipulate dates and times, and get the users local date and time
import datetime

# importing wikipedia which effectively allows us to fetch information on wikipedia
import wikipedia

# importing sys in order to be able to exit the program
import sys

# importing random to make greetings and farewells etc. random
import random

# importing time to allow sleep
import time

#importing requests and json for the map data
import requests, json

# importing the pyautogui library to be able to take a screenshot of the desktop
import pyautogui

# importing os so the user can hibernate computer
import os

#importing ctypes in order to check if microphone is connected
import ctypes
from ctypes import *

# importing wolfram alpha in order to answer mathematical calculations and other queries
import wolframalpha

# setting the objects for speech recognition feature
juun_voice = pyttsx3.init()
voices = juun_voice.getProperty('voices')
juun_voice.setProperty('voice', voices[2].id) # setting the voice, 0 for male and 1 for female
juun_voice.setProperty('rate', 185) # setting the rate of the voice
juun_voice.setProperty('volume', 0.7) # setting the voice's volume where min=0 and max=1
juun_voice.runAndWait()

cwd = os.getcwd()

# creating lists of words/phrases that can be recognised as a command
greeting_words = [
                    "hey",
                    "hello",
                    "hi", 
                    "what's up",
                    "yo",
                    "good morning",
                    "good afternoon",
                    "good evening",
                ]

# creating a list of words/phrases that can be recognised as a command 
farewell_words = [
                    "bye",
                    "goodbye",
                    "i'm leaving june",
                    "no thanks",
                    "no",
                    "no thankyou",
                    "that's all",
                    "no",
                    "never mind",
                    "no that's all thanks",
                    "that's all thanks",
                    "that's all thank you",
                    "no that's all thank you",
                    "that's it",
                    "that's it thanks",
                    "that's it thank you",
                    "no that's it thank you",
                    "exit",
                    "exit program"
                ]

date_words = [
                "what is the date",
                "what's the date",
                "what is the date today",
                "what's the date today",
                "date today",
                "give me the date",
                "date today",
                "tell me the date",
                "date"
            ]

time_words = [   
                "what is the time",
                "what's the time",
                "time please",
                "the time please",
                "tell me the time",
                "time"
            ]

weather_words = [
                    "what is the weather",
                    "what's the weather like",
                    "what is the weather like",
                    "what's the weather like today",
                    "what is the weather like today",
                    "what is the weather today",
                    "weather",
                    "what's the weather",
                    "what's the weather today",
                    "tell me the weather",
                    "is it hot today",
                    "is it hot",
                    "is it cold today",
                    "is it cold",
                    "is it going to be hot today",
                    "is it going to be hot"
                ]

screenshot_words = [
                        "take a screenshot",
                        "screenshot",
                        "take a photo",
                        "take a photo of my screen"
                    ]

email_words = [
                "send an email",
                "email",
]

def internet_connection():
    try: 
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

def microphone_connection():
    winmm= windll.winmm
    num = winmm.waveInGetNumDevs()
    if (num > 0):
        return True
    else:
        return False

# defining the function that allows JUUN to repeat whatever string is passed as a parameter
def juun_say(audio): 
    juun_voice.say(audio)
    juun_voice.runAndWait()

# defining the function that allows JUUN to greet
def juun_greeting():
    greeting_list = [1,2,3,4,5]
    greeting_selection = random.choice(greeting_list)

    if (greeting_selection == 1):
        juun_say("Hello sir, June is here to assist.")   
    elif (greeting_selection == 2):
        juun_say("Hello Isaak.")
    elif (greeting_selection == 3):
        juun_say("Whats up g")
    elif (greeting_selection == 4):
        juun_say("About time you showed up sir")
    elif (greeting_selection == 5):
        juun_say("Hello Sir, I hope you're doing well.")
    else:
        juun_say("Something went wrong, I have to bounce!")
        sys.exit()

# defining the function that allows JUUN to say farewell
def juun_farewell():
    farewell_list = [1,2,3,4,5] 
    farewell_selection = random.choice(farewell_list)

    if (farewell_selection == 1):
        juun_say("Talk to you later sir.")   
    elif (farewell_selection == 2):
        juun_say("Farewell Sir, i'll talk to you later.")
    elif (farewell_selection == 3):
        juun_say("Catch you on the flip side, Isaak")
    elif (farewell_selection == 4):
        juun_say("Peace out, talk soon")
    elif (farewell_selection == 5):
        juun_say("Speak to you soon sir.")
    else:
        juun_say("Something went wrong, I have to bounce!")
        sys.exit()

def juun_anything_else():
    anything_else_list = [1,2,3,4,5] 
    anything_else_selection = random.choice(anything_else_list)

    if (anything_else_selection == 1):
        juun_say("Do you need anything else?")   
    elif (anything_else_selection == 2):
        juun_say("Anything else sir?")
    elif (anything_else_selection == 3):
        juun_say("Do you need help with anything else?")
    elif (anything_else_selection == 4):
        juun_say("Anything else?")
    elif (anything_else_selection == 5):
        juun_say("Need anymore help?")
    else:
        juun_say("Something went wrong, I have to bounce!")
        sys.exit()

# defining the function that picks up the useers voice 
def command():
    rec = sr.Recognizer()

    with sr.Microphone() as source: 
        print("Listening")
        audio = rec.listen(source)

    try:
        print("...")
        phrase = rec.recognize_google(audio, language='en-au')
        print(f"You said {phrase}")
    except Exception as exep:
        print("Can you please repeat that")
        return "None"

    return phrase

# The main function
def JUUN():
    while True:
        # ensuring all commands are in lower case to make conditionals easier to check and guarantee a result
        comnd = command().lower()

        if (comnd == 0):
            continue
        
        # if user says any of the farewell words, such as goodbye, that's all etc.
        if (comnd in farewell_words):
            juun_farewell()
            break
        # if the user replies yes to "anything else sir?"
        elif ("yes" in comnd):
            juun_say("how can i help?")

        elif ("how are you" in comnd):
            juun_say("As good as a computer can be.")
        
        # if the user says any of the greeting words such as hi, hello etc.
        elif (comnd in greeting_words):
            juun_greeting()
            continue

        # if the user wishes to open a website
        elif ("open" in comnd):
            juun_say("opening " + comnd[5:])
            wb.get('opera').open_new_tab(comnd[5:].replace(" ","")+".com")
            time.sleep(1)
            juun_say(comnd[5:]+" opened")
            juun_anything_else()

        #if the user wishes to search the internet for something
        elif ("look up" in comnd):
            wb.get('opera').open_new_tab(f"https://www.google.com.tr/search?q={comnd[7:]}")
            juun_say("searching the web for " + comnd[7:])
            time.sleep(1)
            juun_anything_else()
        # has to be a different elif block or the slicing does not work
        elif("search" in comnd):
            wb.get('opera').open_new_tab(f"https://www.google.com.tr/search?q={comnd[6:]}")
            juun_say("searching the web for " + comnd[6:])
            time.sleep(1)
            juun_anything_else()
        # has to be a different elif block or the slicing does not work
        elif("google" in comnd):
            wb.get('opera').open_new_tab(f"https://www.google.com.tr/search?q={comnd[6:]}")
            juun_say("searching the web for " + comnd[7:])
            time.sleep(1)
            juun_anything_else()
            
        # if the user wishes to know the date
        elif (comnd in date_words):
            today = datetime.date.today()
            date = today.strftime("%B %d, %Y")

            juun_say("the date is" + date)
            time.sleep(0.5)
            juun_anything_else()

        # if the user wishes to know the time
        elif (comnd in time_words):
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M")
            juun_say("the time is " + current_time)
            time.sleep(0.5)
            juun_anything_else()

        # if the user wishes to know the weather
        elif (comnd in weather_words):
            api_key = "f304675e38e3ddbaaa1ca327489eb9c8"
            url = "http://api.openweathermap.org/data/2.5/weather?"
            city = "adelaide"
            full_url = url + "appid=" + api_key + "&q=" + city
            response = requests.get(full_url)
            x = response.json()

            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                celcius = current_temperature - 273.15
                temperature_result = "{:.0f}".format(celcius)
                juun_say("The temperature in adelaide is " + str(temperature_result) + " degrees")
                print("The temperature in adelaide is " + str(temperature_result) + " degrees")
            else: 
                juun_say("something went wrong")

            juun_anything_else()
            
        # if the user wishes to take a screenshot of the screen
        elif (comnd in screenshot_words):
            screenshot = pyautogui.screenshot()
            screenshot.save(f"{cwd}\\Screenshots\\screenshot.png")
            juun_say("Screenshot taken")
            time.sleep(0.7)
            juun_anything_else()

        # if the user wishes to turn the computer to sleep
        elif ("go to sleep" in comnd):
            juun_say("sending computer to sleep")
            time.sleep(1)
            juun_farewell()
            os.system(r'rundll32.exe powrprof.dll,SetSuspendState Sleep')
            sys.exit()

        # if the user wishes to ask JUUN who she is 
        elif ("who are you" in comnd ):
            juun_say("I am june, your personal virtual assistant.")
            time.sleep(0.7)
            juun_anything_else()
        
        # if the user wishes to ask JUUN what her name is
        elif ("what is your name" in comnd or "what's your name" in comnd or "do you have a name" in comnd):
            juun_say("My name is June.")
            time.sleep(1)
            juun_anything_else()

        # if the user wishes to ask JUUN what she is
        elif ("what are you" in comnd):
            juun_say("I am a virtual asssistant, a program, made of one's and zeroes, to help you.")
            time.sleep(1)
            juun_anything_else()

        # if the use wishes to ask who created her
        elif ("who created you" in comnd or "who is your creator" in comnd):
            juun_say("I was created by Isaak Goodwin")
            time.sleep(1)
            juun_anything_else()

        # if the user wishes to ask JUUN what she can do
        elif("what can you do" in comnd or "commands list" in comnd or "commands" in comnd):
            juun_say("Are you ready? I can: Tell you the time\nTell you the weather\nGoogle something\nOpen a website\nTake a screenshot of your screen\nPut the computer to sleep\nopen emails\nask common knowledge question or mathematical question")
            time.sleep(1)
            juun_anything_else()

        # if the user wishes to open emails (gmail)
        elif (comnd in email_words):
            juun_say("Opening emails for you")
            wb.get('opera').open_new_tab("gmail.com")
            time.sleep(1)
            juun_anything_else()

        # if the user wishes to ask JUUN a mathematical or common question
        elif ("can you tell me" in comnd):
            juun_voice.setProperty('rate', 150) # setting the rate of the voice
            question = comnd[15:]
            app_id = "Y7KL6W-2KRAUL8HKY"
            client = wolframalpha.Client("Y7KL6W-2KRAUL8HKY")
            res = client.query(question)
            answer = next(res.results).text
            juun_say(answer)
            print(answer)
            juun_anything_else()

        # adds a note to the JUUN_NOTES.txt file for the user
        elif ("note this for me" in comnd or "note this" in comnd or "note something for me" in comnd):
            juun_say("what would you like me to note?")
            answer = command()
            juun_say("Noted.")
            file_object = open(f'{cwd}JUUN_NOTES.txt', 'a')
            file_object.write(f"\n#idea: {answer}")
            file_object.close()
            juun_anything_else()

        elif (comnd not in farewell_words and "yes" not in comnd 
                and comnd not in greeting_words and "open" not in comnd 
                and "look up" not in comnd and comnd not in date_words 
                and comnd not in time_words and comnd not in weather_words
                and "go to sleep" not in comnd and comnd not in screenshot_words
                and "who are you" not in comnd and "what is your name" not in comnd
                and "what are you" not in comnd and "what's your name" not in comnd
                and "do you have a name" not in comnd and "who is your creator" not in comnd
                and "who created you" not in comnd and "what can you do" not in comnd
                and "commands list" not in comnd and comnd not in email_words 
                and "commands" not in comnd and "can you tell me" not in comnd and "note this for me" not in comnd
                and "note this" not in comnd and "note something for me" not in comnd):
            juun_say("I'm sorry, i dont understand.")

            # used this as dev to create ideas if i said a command and it didn't work
            '''reply = command()

            if (reply == "yes" or command == "yes please"):
                juun_say("Noted.")
                file_object = open(f'{cwd}\JUUN_IDEAS.txt', 'a')
                file_object.write(f"\n#idea: {comnd}")
                file_object.close()
                juun_anything_else()
            elif (reply == "no" or reply == "no thankyou"):
                juun_say("No worries.")
                juun_anything_else()'''

def program_run():
    juun_say("June Virtual Assistant Online")
    while True:
        res = command()
        if (res == "hey June"):
            juun_say("How can I help?")
            JUUN()
        elif (res == "June turn off" or res == "turn off" or res == "exit"):
            break
        else:
            continue

from tkinter import *

root= Tk()

canvas = Canvas(root, width = 500, height = 300)
canvas.pack()
root.resizable(width=False, height=False)
root.eval('tk::PlaceWindow . center')

bg = PhotoImage(file = f"{cwd}\Media\Images\main_logo.png")

label1 = Label( root, image = bg)
label1.place(x = 0, y = -100)
    
def close_app():
    sys.exit()

Button(root, text="RUN", bg='#0083EE', fg='white', activebackground='#124F88',activeforeground='white', padx=20, pady=3, command=program_run).place(x=170, y=260)
Button(root, text="EXIT", bg='#0083EE', fg='white', activebackground='#124F88',activeforeground='white', padx=20, pady=3, command=close_app).place(x=250, y=260)


photo = PhotoImage(file = f"{cwd}\Media\Images\JUUN_Icon.png")
root.iconphoto(False, photo)



# running primary code
if __name__=='__main__':
    # startup
    print("#########################################################")
    print(" ")

    # checking internet connection
    print("Checking stable internet connecton...")
    if (internet_connection()):
        print("Internet connection detected")
        print(" ")
        #time.sleep(1.5)
    else:
        time.sleep(3)
        print("No internet connection detected")
        print("Please ensure you have an internet connection.")
        print("Shutting down...")
        print(" ")
        time.sleep(2)
        print("#########################################################")
        sys.exit()
    
    # checking microphone connection
    print("Checking microphone connection...")
    if (microphone_connection()):
         print("Microphone connection detected")
         print(" ")
         #time.sleep(1.5)
    else:
        time.sleep(3)
        print("No microphone connection detected")
        print("Please ensure you have a microphone connection.")
        print("Shutting down...")
        print(" ")
        time.sleep(2)
        print("#########################################################")
        sys.exit()

    print("#########################################################")
    print("")
    print("WELCOME, I AM")
    print(" ")
    print('  888888   888     888   888     888   888b    888 ')
    print('    "88b   888     888   888     888   8888b   888 ')
    print('     888   888     888   888     888   88888b  888')
    print('     888   888     888   888     888   888Y88b 888 ')
    print('     888   888     888   888     888   888 Y88b888 ')
    print('     888   888     888   888     888   888  Y88888 ')
    print('     88P   Y88b. .d88P   Y88b. .d88P   888   Y8888 ')
    print('     888    "Y88888P"     "Y88888P"    888    Y888   v0.1.0')
    print('   .d88P')
    print(' .d88P"')
    print('888P"')
    print(" ")
    print("YOUR PERSONAL, VIRTUAL ASSISTANT.")
    print(" ")
    print('SAY "Commands" FOR A LIST OF COMMANDS')
    print("#########################################################")

    root.mainloop()













 





                                    
                                     
                                        






