# importing the speech recognition library that is able to listen to the users microphone and register what the user is saying
import speech_recognition as sr
# importing pyttsx3 which basically onverts text to speech
import pyttsx3
# importing webbrowser which opens web broswers in another window in the users default browser
import webbrowser
#importing datetime which allows us to manipulate dates and times, and get the users local date and time
import datetime
# importing wikipedia which effectively allows us to fetch information on wikipedia
import wikipedia
# importing sys in order to be able to exit the program
import sys
# importing random to make greetings and farewells etc. random
import random

# setting the objects for each feature
juun_voice = pyttsx3.init()
voices = juun_voice.getProperty('voices')
juun_voice.setProperty('voice', voices[3].id) # setting the voice, 0 for male and 1 for female
print(voices[1].id)
juun_voice.setProperty('rate', 185) # setting the rate of the voice
juun_voice.setProperty('volume', 0.7) # setting the voice's volume where min=0 and max=1
juun_voice.runAndWait()

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
        juun_say("Whats up Isaak.")
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
        juun_say("Farewell Sir, ill talk to you later.")
    elif (farewell_selection == 3):
        juun_say("Catch you on the flip side Isaak")
    elif (farewell_selection == 4):
        juun_say("Peace out, talk soon")
    elif (farewell_selection == 5):
        juun_say("Speak soon sir.")
    else:
        juun_say("Something went wrong, I have to bounce!")
        sys.exit()

# defining the function that authorises the user upon start-up
def authorisation():
    authorised = False;
    juun_say("June awoken. Please authorise yourself.")
    
    while (authorised == False):
        if (audio_input == "kane 17"):
            juun_greeting()
            authorised = True
        elif (audio_input == "terminate"):
            juun_farewell()
            sys.exit()
            break
        else:
            juun_say("authorisation failed, try again")
            continue

# defining the function that picks up the useers voice 
def audio_input():
    aud = sr.Recognizer()

    with sr.Microphone() as source: 
        print("Listening and processing...")

    audio = aud.listen(source)

    try:
        print("understanding")
        phrase = aud.recognize_google(audio, language='en-au')
        print("you said: ", phrase)
    except Exception as exp:
        print(exp)
        print("Can you please repeat that")
        return "None"
    
    return phrase






