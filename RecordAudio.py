import pyaudio
import wave

# Define the audio settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
WAVE_OUTPUT_FILENAME = "input.wav"

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open the audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

frames = []
is_recording = False

print("Press 'r' to start recording...")

# Start recording while the user is pressing the R key
while True:
    try:
        key = input()
        if key == 'r':
            if not is_recording:
                is_recording = True
                print("Recording started...")
            else:
                is_recording = False
                print("Recording stopped...")
                break

        if is_recording:
            data = stream.read(CHUNK)
            frames.append(data)

    except KeyboardInterrupt:
        break

# Stop the stream and close PyAudio
stream.stop_stream()
stream.close()
p.terminate()

# Save the recorded audio to a WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
