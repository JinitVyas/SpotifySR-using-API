from dotenv import load_dotenv
import os
import base64
from requests import post
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type"  : "application/x-www-form-urlencoded"
    }

    data = {"grant_type" : "client_credentials"}
    result = post(url, headers = headers, data =data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

t = get_token()
print(t)

# So far, 
'''
    we imported 
        dotenv to get data from .env file
        os to access the env file
        base64 to convert request into bytes
        requests to request to the server
        json to access the json response from server
        
    then, 
        we loaded .env file
        and created  variables to store client_id and secret
    
    then created the function get_token()
        in this function,
            we first created auth_string using .env variables(client credentials)
            then encoded it to bytes
            then converted the encoded bytes back to string 
            THE ENCRYPTION DONE ✅
        
            then provided url endpoint to send request and headeres of the request and data containing "client_creadentials" as "grant_type"

            then a post request is sent to the (url) with headers=headers and data=data
            
            then json_result stored the result.content

            then accessed the token and returned it.
            
'''