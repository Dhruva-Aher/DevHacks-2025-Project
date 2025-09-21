import flet as ft
import homeScreen
import audio
import request

def micButtonClick(e):
    print("Mic clicked!")
    audio.record_audio()

def cancelButtonClick(e):
    print("Cancelling...")
    audio.stop_audio()
    text = audio.audio_to_text()
    print(text)
    questions = request.get_icebreakers(text)
    print(questions)
