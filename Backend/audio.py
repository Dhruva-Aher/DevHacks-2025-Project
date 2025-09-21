import speech_recognition as sr
import time

recognizer = sr.Recognizer()
mic = sr.Microphone()

silence_limit = 5  # seconds
chunk_duration = 1  # seconds per chunk

with mic as source:
    print("Adjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Start speaking:")

    audio_chunks = []
    last_sound_time = time.time()
    stop_detected = False

    while True:
        audio = recognizer.listen(source, phrase_time_limit=chunk_duration)
        audio_chunks.append(audio)

        # Try to recognize right after each chunk
        try:
            text = recognizer.recognize_google(audio)
            print("Heard chunk:", text)
            if "stop" in text.lower():
                print("Detected keyword 'stop', stopping...")
                stop_detected = True
                break
            last_sound_time = time.time()  # Only update on successful recognition
        except sr.UnknownValueError:
            # If the chunk is not recognized, it's likely silence or noise
            pass
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

        if time.time() - last_sound_time > silence_limit:
            print("Detected 5 seconds of silence, stopping...")
            break

if audio_chunks:
    full_audio = sr.AudioData(
        b"".join(chunk.get_raw_data() for chunk in audio_chunks),
        audio_chunks[0].sample_rate,
        audio_chunks[0].sample_width
    )

    try:
        text = recognizer.recognize_google(full_audio)
        print("Full transcription:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
else:
    print("No audio captured.")