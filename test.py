from dotenv import load_dotenv
import os
import base64
import requests
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

def get_song_details(song_name, access_token):
    search_url = "https://api.spotify.com/v1/search/"
    parameters_of_query_string = {
        'q': song_name,
        'type': 'track',
        'limit': 1 
    }
    headers = {'Authorization': f'Bearer {access_token}'}
    result = requests.get(search_url, parameters_of_query_string, headers=headers)
    
    if result.status_code == 200:
        track_details = result.json()
        t_id = track_details["tracks"]["items"][0]["id"]
        t_name = track_details["tracks"]["items"][0]["name"]
        artists = track_details["tracks"]["items"][0]["artists"]
        
        print(f"\n\n{t_id}\n<'{t_name}'> by <'{artists[0]['name']}'>")
        return t_id
    else:
        print(f"****************************error: {result} ****************************")

song_name = input("Enter a song name: ")
t_id = get_song_details(song_name, t)

def get_features(track_id, access_token):
    
    # Preparing the request to send for audio features
    features_url = f'https://api.spotify.com/v1/audio-features/{track_id}'
    headers = {'Authorization': f'Bearer {access_token}'}
    
    # Sending a request and getting a response
    response = requests.get(features_url, headers=headers)
    
    if response.status_code == 200:
        print("YOOOOOO")
        audio_features = response.json()
        print( audio_features)
    else:
        print("NOOOOOOOO")
get_features(t_id, t)