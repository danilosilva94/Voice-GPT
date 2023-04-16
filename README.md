# Voice-GPT

## Introduction
Voice-GPT is a Python program that allows you to interact with OpenAI's powerful GPT-3.5 model using your voice on a Raspberry Pi. With Voice-GPT, you can record your questions using your microphone, and the program will transcribe your audio, send the text to the GPT-3.5 model for processing, and then play back the response as speech through your speakers.

## Dependencies

Before running the program, you'll need to install the following dependencies:

- pyaudio
- libportaudio2
- SpeechRecognition
- openai
- pyttsx3
- flac
- espeak

You can install these dependencies using the following command in your terminal:

```
pip install pyaudio && sudo apt-get install libportaudio2 && pip install SpeechRecognition && pip install openai && pip install pyttsx3 && sudo apt-get install flac && sudo apt-get install espeak
```

## Usage
To use the Voice-GPT program, follow these steps:

Get an API key from OpenAI.
Run the start.py file using the following command in your terminal:

```
python Start.py
```

Press the 'r' key to start recording your question. You'll have 5 seconds to record your question before the program saves your audio to a file called input.wav.
The program will transcribe your recorded audio to text and send it to the GPT-3.5 model for processing.
The program will then speak the response back to you through your speakers.
You can press 'r' as many times as you want to ask more questions. If you want to quit the program, press the 'q' key.

## Conclusion
I hope you find Voice-GPT to be a fun and interactive way to experiment with AI using your voice. Feel free to modify the program to suit your needs, and don't hesitate to reach out if you have any questions or feedback!
