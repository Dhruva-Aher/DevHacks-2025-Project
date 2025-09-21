import flet as ft
import Backend.audio as audio
import Backend.request as request

icebreaker_questions="Model is Processing ..."

def micButtonClick(e):
    print("Mic clicked!")
    audio.record_audio()

def cancelButtonClick(e):
    global icebreaker_questions
    print("Cancelling...")
    audio.stop_audio()
    text = audio.audio_to_text()
    print(text)
    icebreaker_questions = request.get_icebreakers(text)
    print(icebreaker_questions)
