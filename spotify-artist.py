#1. importing libraries needed
import requests

#2. the acccess token generated through your OAuth process from previous script
ACCESS_TOKEN = " "

#3. spotify artist ID for Travis Scott
artist_id = "0Y5tJX1MQlPlqiwlOH1tJY" 

#4. spotify api URL for the artist
artist_url = f"https://api.spotify.com/v1/artists/" + artist_id

#5. headers for the request, including the Authorization token
headers = {
    "Authorization": "Bearer " + ACCESS_TOKEN
}

#6. making the GET request
response = requests.get(artist_url, headers=headers)

#7. printing the response (artist details)
print(response.json())
