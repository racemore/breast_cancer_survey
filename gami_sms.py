import json
from twilio.rest import Client
from decouple import config

ACCOUNT_SID = config('ACCOUNT_SID')
AUTH_TOKEN = config('AUTH_TOKEN')
ASSISTANT_ID = config('ASSISTANT_ID')
client = Client(ACCOUNT_SID, AUTH_TOKEN)
                
queries = client.autopilot \
                .assistants(ASSISTANT_ID) \
                .queries \
                .list(limit=100)

users = []
for record in queries:
    sender_id = record.dialogue_sid
    user_data = {"sender_id":sender_id}
    user_data |= record.results
    users.append(user_data)

json_object = json.dumps(users)

with open("all_queries.json", "w") as outfile:
    outfile.write(json_object)