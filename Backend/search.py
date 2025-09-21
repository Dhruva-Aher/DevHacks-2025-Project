#from supermemory import AsyncSupermemory
from supermemory import Supermemory
import asyncio

#import request
#import os

# client = AsyncSupermemory(
#     api_key="sm_opamYwWLBTUQt52p3eQLTs_PqTVisjbloPVfuqYMbeVRkJomfBQmMKyspkqWWprSIonTuRYHRVagLoadJKOBdyE",
# )

client = Supermemory(
    api_key="",
    base_url="https://api.supermemory.ai/"
)

search_response = client.search.execute(
     q="What do I like to do?",
)
print(search_response.results)
