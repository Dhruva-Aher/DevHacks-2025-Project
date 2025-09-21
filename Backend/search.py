#from supermemory import AsyncSupermemory
from supermemory import Supermemory
import asyncio
from dotenv import load_dotenv
#import request
import os


# Load environment variables
load_dotenv()

client = Supermemory(
    api_key = os.environ.get("SUPERMEMORY_API_KEY"),
    base_url = "https://api.supermemory.ai/"
)

search_response = client.search.execute(
     q = "What do I like to do?",
)
print(search_response.results)
