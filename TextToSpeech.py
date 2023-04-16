import pyttsx3

# Initialize the text to speech engine
engine = pyttsx3.init()

# Speak the specified text
engine.say('Hello World!')

# Run the text to speech engine
engine.runAndWait()