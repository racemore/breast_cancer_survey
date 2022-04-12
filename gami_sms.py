

import os
import json
from twilio.rest import Client
from decouple import config
import requests
from json import JSONEncoder

class QueryEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

# ACCOUNT_SID = os.getenv('ACCOUNT_SID')
# AUTH_TOKEN = os.getenv('AUTH_TOKEN')
# ASSISTANT_ID = os.getenv('ASSISTANT_ID')
ACCOUNT_SID = config('ACCOUNT_SID')
AUTH_TOKEN = config('AUTH_TOKEN')
ASSISTANT_ID = config('ASSISTANT_ID')
client = Client(ACCOUNT_SID, AUTH_TOKEN)
                
queries = client.autopilot \
                .assistants(ASSISTANT_ID) \
                .queries \
                .list(limit=100)

lst = []
for record in queries:
    sender_id = record.dialogue_sid
    msg_dct = {"sender_id":sender_id}
    msg_dct |= record.results
    lst.append(msg_dct)

json_object = json.dumps(lst)

with open("all_queries.json", "w") as outfile:
    outfile.write(json_object)