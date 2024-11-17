# Voice Assistant - Shiva

This project implements a simple voice assistant, **Shiva**, built using Python. The assistant can perform various tasks based on voice commands, such as playing YouTube videos, telling jokes, looking up information on Wikipedia, checking the current time, and searching on Google. The assistant is designed to be activated by the wake word "shiva" and responds using text-to-speech.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)


## Features

- **Wake Word Detection**: Listens for the wake word "shiva" to activate the assistant.
- **Text-to-Speech (TTS)**: Provides spoken responses using the `pyttsx3` library.
- **Voice Command Recognition**: Listens for user input and converts speech to text using `speech_recognition`.
- **Play YouTube**: Plays YouTube videos using `pywhatkit`.
- **Tell Jokes**: Tells jokes using the `pyjokes` library.
- **Wikipedia Search**: Retrieves information from Wikipedia using the `wikipedia` library.
- **Time Check**: Provides the current time.
- **Google Search**: Searches for queries using `pywhatkit`'s Google search functionality.
- **Error Handling**: Responds with "I didn't catch that" if the command is not recognized.

## Technologies Used

- **Python**: The programming language used to implement the voice assistant.
- **SpeechRecognition**: Used for converting speech to text.
- **pyttsx3**: Used for converting text to speech (TTS).
- **pywhatkit**: Used to play YouTube videos and search on Google.
- **pyjokes**: Used to fetch jokes for the user.
- **wikipedia**: Used to fetch information from Wikipedia.
- **datetime**: Used to get the current time.
- **winsound**: Used to play a beep sound when the assistant is activated.

## How It Works

1. **Wake Word Detection**: The assistant continuously listens for the wake word "shiva". Once heard, it activates and plays a beep sound.
2. **Voice Command Processing**: After activation, the assistant listens for commands and responds accordingly:
   - If the user asks for "your name" or "who are you", it responds with "My name is Shiva".
   - If the user asks to "play [song or video]", it plays the video on YouTube.
   - If the user asks for a "joke", it tells a joke.
   - If the user asks "who is [name]" or "what is [topic]", it retrieves information from Wikipedia.
   - If the user asks "what is the time", it tells the current time.
   - If the user asks about "google", "meaning", or "search", it searches for the query on Google.
3. **Error Handling**: If the assistant does not recognize a command, it responds with "I didn't catch that".
