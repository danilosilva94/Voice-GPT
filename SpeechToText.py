import speech_recognition as sr

def transcribe_audio(filename):
    # Initialize the speech recognizer
    r = sr.Recognizer()

    # Open the input WAV file
    with sr.AudioFile(filename) as source:
        # Read the audio data from the file
        audio_data = r.record(source)
        try:
            # Use the Google Speech Recognition API to convert speech to text
            text = r.recognize_google(audio_data)
            # Print the resulting text
            print("You said: ", text)
            return text
        except sr.UnknownValueError:
            print("Unable to transcribe audio")
