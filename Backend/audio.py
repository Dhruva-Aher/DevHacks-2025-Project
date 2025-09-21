import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import speech_recognition as sr

fs = 44100
filename = "output.wav"

def record_audio():
    print("Recording... Press Enter to stop")
    recording = []

    def callback(indata, frames, time, status):
        recording.append(indata.copy())

    with sd.InputStream(samplerate=fs, channels=1, callback=callback):
        input()  # stop on Enter********************************************************************

    audio_data = np.concatenate(recording, axis=0)

    # Convert float32 array to int16
    audio_data = np.int16(audio_data * 32767)

    write(filename, fs, audio_data)
    print(f"Recording saved as {filename}")

def audio_to_text():
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            print("Transcribed Text:", text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"API error: {e}")
    return text

#record_audio()
#text = audio_to_text()
