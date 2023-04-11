import pyaudio
import wave

# Define the audio settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "input.wav"

# Initialize PyAudio
p = pyaudio.PyAudio()
    
#Open the audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=1,
                frames_per_buffer=CHUNK)

frames = []

# Record audio for the specified duration
print("Recording Started...")
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording Finished...")

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