import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import wikipedia
import datetime

talkback = pyttsx3.init()
talkback.setProperty('rate',155)
recognizer = sr.Recognizer()
voices = talkback.getProperty('voices')
talkback.setProperty('voice', voices[1].id)
def talk(content):
    talkback.say(content)
    talkback.runAndWait()

def active():
    try:
        with sr.Microphone() as mic:
            voice = recognizer.listen(mic)
            com = recognizer.recognize_google(voice).lower()
            # print(com)
            if 'your name' in com or 'who are you' in com:
                talk('My name is jhon')
            elif 'play' in com:
                com = com.split('play')[1]
                pywhatkit.playonyt(com)
            elif 'joke' in com:
                if 'tell' in com:
                    talk(pyjokes.get_joke())
                    # print("hi")
            elif 'who is' in com:
                person = com.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'what is' in com and 'time' in com:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
            elif 'what is' in com:
                person = com.replace('what is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'google' in com:
                com = com.split('google')[1]
                pywhatkit.search(com)
            else:
                talk("I didn't catch that")
    except:
        pass
talk("I'm online")
talk('What can i do for you')
def main():
    while True:
        active()

main()