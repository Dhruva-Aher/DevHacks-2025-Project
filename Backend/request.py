from google import genai
from supermemory import Supermemory
#import audio
import os
from dotenv import load_dotenv
from frontPageForm import userNamePassword


# Load environment variables
load_dotenv()

#Google Gemini Request ----------------------------------------------
def get_icebreakers(text):
    #audio.record_audio()
    #text = audio.audio_to_text()
    # sample_text = "Hello my name is prince, I am majoring in computer science, I take computer science"
    prefix_question = "Form exactly 5 Icebreaker questions, based the following user conversation, to continue the conversation."
    content = prefix_question + text

    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"), 
                          http_options={"base_url": "https://api.supermemory.ai/v3/https://generativelanguage.googleapis.com", 
                                        "api_version": "v1", 
                                        "headers": {
                                            "x-supermemory-api-key": os.environ.get("SUPERMEMORY_API_KEY"),
                                            'x-sm-user-id': userNamePassword["enguyen"]
                                        }})

    response = client.models.generate_content(
	    model="gemini-2.5-flash",
	    contents=content
    )
    generated_text = response.text



    #Supermemory Storage -------------------------------------------

    sm_client = Supermemory(api_key=os.environ.get("SUPERMEMORY_API_KEY"), 
                            base_url="https://api.supermemory.ai/")
    training_info = content + generated_text
    store_response = sm_client.memories.add(content=training_info)

    return generated_text


#questions = get_icebreakers()
#print(questions)


"""
#client = genai.Client(api_key=os.getenv(GEMINI_API_KEY))
#api_key=os.getenv(SUPER_MEMORY_KEY)
"""
