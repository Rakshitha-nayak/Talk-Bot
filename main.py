# TALK BOT
"""
Created on Mon May 17 22:59:26 2021

@author: RAKSHITHA NAYAK
"""
#import required packages
import pyttsx3 #text-to-speech library
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5') #Microsoft developed speech API.Helps in synthesis and recognition of voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #Voice id helps us to select different voices. 
                                          #voice[0].id = Male voice 
                                          #voice[1].id = Female voice

#speak() function will take audio as an argument, and then it will pronounce it.
def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.

#we will make a wishme() function, that will make the Talk-Bot. wish or greet the user according to the time of computer or pc.
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

    print("Please tell me how may I help you") 
    speak("Please tell me how may I help you")

#we will make a takeCommand() function.  With the help of the takeCommand() function, the Talk-Bot will return a string output by taking microphone input from the user.       
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n") #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice
        return "None" #None string will be returned
    return query

'''
Simple Mail Transfer Protocol (SMTP) is a protocol that allows us to send emails and to route emails between mail servers.
An instance method called sendmail is present in the SMTP module. 
This instance method allows us to send an email.
It takes 3 parameters:
The sender: Email address of the sender.
The receiver: T Email of the receiver.
The message: A string message which needs to be sent to one or more than one recipient.
'''
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        
       
        #check whether Wikipedia is in the search query of the user or not. 
        #If Wikipedia is found in the user's search query, then two sentences from the 
        #summary of the Wikipedia page will be converted to speech with the speak function's help.
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'tell me about' in query:
            topic = query[14:]
            wiki_res = wikipedia.summary(topic, sentences=1)
            print(wiki_res)
            speak(wiki_res)
            
        elif 'hello' in query:
            print('Hello')
            speak("Hello!")
            
        elif 'hi' in query:
            print('Hi!')
            speak("Hi!")

        elif 'how are you' in query:
                    li = ['good', 'fine', 'great']
                    response = random.choice(li)
                    print(f"I am {response}")
                    speak(f"I am {response}")
        
        
        #To open any website, we need to import a module called webbrowser.
        #It is an in-built module, and we do not need to install it with a pip statement,
        #we can directly import it into our program by writing an import statement.   
                
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        
        #To play music, we need to import a module called os. 
        #Import this module directly with an import statement.
       
        elif 'play music' in query:
            music_dir = 'C:\\Users\\WIN10\\Music' #music directory
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0])) #plays the first song in directory
        
        #tells the current time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strTime)
            speak(f"the time is {strTime}")
          
        #tells the current date
        elif 'date' in query:
            date = datetime.datetime.now().strftime("%d:%B:%Y")
            print(date)
            speak(f"the date is {date}")
            
        elif 'who are you' in query:
            print("I am your personal assistant")
            speak("I am your personal assistant")

        elif 'email to' in query:
            try:
                name = query[9:]
                speak("What should I say?")
                content = takeCommand()
                to = f"{name}@gmail.com"  
                print(to)
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")  
        
        #ends the conversatiom\terminates the program
        elif "stop listening" in query:
            print("Okay")
            speak("Okay")
            break
