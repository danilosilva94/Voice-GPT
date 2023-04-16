import pyttsx3

def speak(text):
    # Initialize the text to speech engine
    engine = pyttsx3.init()

    # Speak the specified text
    print("They said", text)
    engine.say(text)

    # Run the text to speech engine
    engine.runAndWait()