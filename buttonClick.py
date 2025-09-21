import flet as ft
#import homeScreen
import audio
import request

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
