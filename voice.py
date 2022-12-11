import speech_recognition
import pyttsx3
import os
import openai




recognizer = speech_recognition.Recognizer()
f = open("voice_transcript.txt", "a")


while True:

    try:

        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            print(f"I detected: {text}")
            f.write(text + "\n")

    
    except speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        print("No speech detected - terminating")
        f.close()
        continue
        