import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import wikipedia
import datetime
import winsound

talkback = pyttsx3.init()
talkback.setProperty('rate',155)
recognizer = sr.Recognizer()
voices = talkback.getProperty('voices')
talkback.setProperty('voice', voices[1].id)

def talk(content):
    talkback.say(content)
    talkback.runAndWait()

def rewrite(text):
    words = ['of', 'what', 'does', 'is', 'the', 'search', 'mean', 'meaning', 'google', 'for']
    for i in words:
        text = text.replace(i, '')
    return text

def listen1():
    try:
        with sr.Microphone() as mic:
            voice = recognizer.listen(mic, phrase_time_limit=2)
            command = recognizer.recognize_google(voice).lower()
            print(command)
            return command
    except:
        return ''
        pass

def listen():
    try:
        with sr.Microphone() as mic:
            voice = recognizer.listen(mic, phrase_time_limit=6)
            command = recognizer.recognize_google(voice).lower()
            return command
    except:
        return ''
        pass


def active():
            com = listen()
            print(com)
            if 'your name' in com or 'who are you' in com:
                talk('My name is shiva')
            elif 'play' in com:
                com = com.replace('play', '')
                text = 'playing ' + com
                talk(text)
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
            elif 'time' in com:
                    if 'what is' in com or "what's" in com:
                        time = datetime.datetime.now().strftime('%I:%M %p')
                        talk('Current time is ' + time)
            elif 'what is' in com:
                person = com.replace('what is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'google' in com or 'mean' in com or 'meaning' in com:
                com = com.replace('google', '')
                com = rewrite(com)
                print(com)
                pywhatkit.search(com)
            else:
                talk("I didn't catch that")


def main():
    talk('Online')
    while True:
            check = listen1()
            if 'shiva' in check:
                frequency = 2500
                duration = 1000  
                winsound.Beep(frequency, duration)
                active()


main()


