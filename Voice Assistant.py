import pyttsx3 #Text-to-speech conversion library
import datetime #Date and time library
import speech_recognition as sr #Speech Recognition Library

engine = pyttsx3.init()
''' 
 Initializes variable and gets a reference to an engine [pyttsx3.Engine which provides application access to text-to-speech synthesis.]
(An engine executes code using pre-loaded interpreter in a safe sandboxed environment 
(sandboxing isolates app for security and servicce and to prevent system malfunction)) 
instance(individual object) that will use the given driver(pyttsx3 in this case)
'''

"""VOICE"""
voices = engine.getProperty('voices') #gets details of current voices
#print(tuple(voices)) #Prints list of voice options avalaible
engine.setProperty('voice', voices[1].id) #Gets voice in specified index value from voices list
#[7] & [0] are best male voices, [36] is best female voice ([20] & 39] are female Indian voices)
#engine.setProperty('voice', voices[0].id)  
#engine.setProperty('voice', voices[1].id)   



def name():
    engine.say("I am Socrates. No, like, seriously, that's what I am called")
    engine.runAndWait()
#name()

def time():
    Time = datetime.datetime.now().strftime("%I:%M %p") #Gives (current) time as of present in specified format (Hours : Minutes : Seconds)
    print("The time is", Time)
    engine.say("The time is")
    engine.say(Time)
    engine.runAndWait()

#time()


def date():
    date_today=datetime.datetime.now() #Gets current date and time
    engine.setProperty('rate',250)
    print("Today is", date_today.strftime("%A" ","), date_today.strftime("%d" "") , date_today.strftime("%B"), date_today.year)
    engine.say("Today is")
    engine.say(date_today.strftime("%A" ",")) #Returns full name of weekday
    engine.say(date_today.strftime("%d" "")) #Returns day of month/date as a numerical value
    engine.say(date_today.strftime("%B")) #Returns full name of month
    engine.say(date_today.strftime("%Y)")) #Returns year with century
    engine.runAndWait()
#date()  


def greet():
    hour = datetime.datetime.now().hour #Gets current hour (24 hour format)
    if hour>4:
        if hour<12:
            print("Good morning")
            engine.say("Good morning")
            engine.runAndWait()
            audio = r.listen(source)
            
        if hour>=12:
            if hour<17:
                print("Good afternoon")
                engine.say("Good afternoon")
                engine.runAndWait()
                audio = r.listen(source)
    if hour>16:
        if hour<24:
            print("Good evening")
            engine.say("Good evening")
            engine.runAndWait()
            audio = r.listen(source)
            
    if hour<4:
        print("Good night")
        engine.say("Good night")
        engine.runAndWait()
        audio = r.listen(source)

greet()

def intro():
    engine.say("I am an AI assistant developed to help make your life easier and give those fingers a break from having to type everything. I am still learning, so pardon me if I am unuae to respond to some of your queries")

def database():
    engine.say("Creating database")
    db={}
    n=int(input("Enter number of items:"))
    for i in range (n):
        Key=eval(input("Enter key:"))
        Val=eval(input("Enter item value:"))
        db.update({Key: Val})
        i+=1
    engine.say("The following database has been created")
    print("The following database has been created:")
    print(db)

database()

while True:
    r = sr.Recognizer() #Object with function to recognize audio/speech
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio format
        query=r.recognize_google(audio)

        print("You said " + query)    # recognizes speech using Google Speech Recognition

        #except LookupError:                           # speech is unintelligible
           # print("Could not understand audio")

        if 'name' in query:
            name()

        if 'date' in query:
            date()

        if 'time' in query:
            time()

        if 'who are you' in query:
            intro()

        if 'database' in query:
                database()            
