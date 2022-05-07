import speech_recognition as sr
import pyttsx3#convert the audio to text
import pywhatkit#bundle of kitt of take the Q from user
import datetime
import wikipedia
import pyjokes#from jiokes (python joke)

listener=sr.Recognizer()#here we are listening
engine=pyttsx3.init()#converting the voice into text
voices=engine.getProperty('voices')#setting the perporty of Alexa(talking bot)
engine.setProperty('voice',voices[1].id)#0 for male and 1 for female voice
#defination for talk of bot
def talk(text):
    engine.say(text)
    engine.runAndWait()


#command taking from user as Voice
def take_command():
    try:
        with sr.Microphone() as source:#listening from the local system
            print('listening.....')
            voice=listener.listen(source)#saving the voice signal in voice variable
            command=listener.recognize_google(voice)#converting sound singnal in text
            command=command.lower()
            if 'disha' or 'disa' in command:#waht yours bot name (ranjit,alexa,disha like this)#checking whether the command in the bot
                command=command.replace('bot','')
                print(command)
    except:
        print(" I am unable to listen..kindly speak again")
    return command

def run_bot():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'fresh' in command:
        song=command.replace('fresh','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().stftime('%I:%M %P')
        talk("current time is "+time)
    elif 'who are you' in command:

        talk("I am Disa , your  personal assistant version 0.01")
    elif 'who made you' in command:
        talk("I am created by Ranjit ,he is a certified Data Scientist  from here you can find him https://www.linkedin.com/in/ranjit-maity-75204a131/")
    elif 'print' in command:
        print('https://www.linkedin.com/in/ranjit-maity-75204a131/')
    elif 'who' in command:
        person=command.replace('who','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'why' in command:
        reason=command.replace('why','')
        info=wikipedia.summary(reason,5)
        print(info)
        talk(info)
    elif 'how' in command:
        how=command.replace('how','')
        info=wikipedia.summary(how,5)
        print(info)
        talk(info)
    elif 'when' in command:
        when=command.replace('when','')
        info=wikipedia.summary(when,5)
        print(info)
        talk(info)
    elif 'where' in command:
        where=command.replace('where','')
        info=wikipedia.summary(where,5)
        print(info)
        talk(info)
    elif 'whome' in command:
        whome=command.replace('whome','')
        info=wikipedia.summary(whome,5)
        print(info)
        talk(info)
    elif 'what' in command:
        what=command.replace('what','')
        info=wikipedia.summary(what,5)
        print(info)
        talk(info)
    elif 'thnakyou' in command:
        talk("you are welcome")
        exit()
    elif 'bye' in command:
        talk("bye bye")
        exit()
    
    else:
        talk("am  only a talking bot ...am not got")

while True:
    try:
        run_bot()
    except:
        talk("I am unable to listen..kindly speak again")
        statment='Kindly,re-run ,the ,Bot'
        talk(statment)
        print(statment)
        break