import pyttsx3

engine = pyttsx3.init()

# Get a list of available voices
voices = engine.getProperty('voices')

# Set the voice to the second available voice
engine.setProperty('voice', voices[1].id)

# Speak the text
engine.say("Hello, this is some text-to-speech output with a different voice.")
engine.runAndWait()
