from google import genai
from supermemory import Supermemory
#import os
from audio import text

#Google Gemini Request --------------------------------------------------------------------------------
UserID = "User: "
prefix_question = "Form exactly 5 Icebreaker questions, based the following user conversation, to continue the conversation."
content = prefix_question + text
GEMINI_API_KEY = "AIzaSyDfyop-21wkmyErdXMAbS-owlhwO1NeYBE"

#client = genai.Client(api_key=os.getenv(“GEMINI_API_KEY”))
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
	model="gemini-2.5-flash",
	contents=content
)
print(response.text)



#Supermemory Storage -----------------------------------------------------------------------------------

client = Supermemory(
    api_key="sm_opamYwWLBTUQt52p3eQLTs_PqTVisjbloPVfuqYMbeVRkJomfBQmMKyspkqWWprSIonTuRYHRVagLoadJKOBdyE",
    base_url="https://api.supermemory.ai/"
)
training_info = content + response.text

# memory_data = {
#     "id": "Prince",  # you can create a unique ID for this entry
#     "content": training_info
# }

store_response = client.memories.add(content=training_info)
print("Stored in Supermemory:", store_response)