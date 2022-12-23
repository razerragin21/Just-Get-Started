import speech_recognition
import pyttsx3

# Initialize the recognizer and the engine for text to speech
recognizer = speech_recognition.Recognizer()
# open a file to write the voice transcript, append any new text to the end of the file
f = open("voice_transcript.txt", "a")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Create a while loop to keep the program running 
while True:

    try:

        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            print(f"I detected: {text}")
            f.write(text + "\n")
            engine.say(text)
            engine.runAndWait()

    # If the user says "stop" or no speech is detected, break the loop
    except speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        print("No speech detected - terminating")
        # Close the file
        f.close()
        continue



