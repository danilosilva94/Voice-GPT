from RecordAudio import record_audio
from SpeechToText import transcribe_audio
from GPT import generate_response
from TextToSpeech import speak

def main():
    while True:
        key = input("Press 'r' to record and 'q' to quit: ")
        if key.lower() == 'q':
            break
        elif key.lower() == 'r':
            # Record audio for 5 seconds and save it to a file
            filename = "input.wav"
            duration = 5
            record_audio(filename, duration)

            # Transcribe the recorded audio to text
            prompt = transcribe_audio(filename)

            # Ask Chat-GPT
            answer = generate_response(prompt)

            # Speak answer
            speak(answer)

if __name__ == "__main__":
    main()
