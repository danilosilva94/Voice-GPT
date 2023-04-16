import speech_recognition as sr

# Initialize the speech recognizer
r = sr.Recognizer()

# Open the input WAV file
with sr.AudioFile('input.wav') as source:
    # Read the audio data from the file
    audio_data = r.record(source)
    try:
        # Use the Google Speech Recognition API to convert speech to text
        text = r.recognize_google(audio_data)
        # Print the resulting text
        print(text)
    except sr.UnknownValueError:
        print("Unable to transcribe audio")
