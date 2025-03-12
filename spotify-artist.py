import requests

# The Access Token generated through your OAuth process
ACCESS_TOKEN = " "

# Spotify Artist ID for Travis Scott
artist_id = "0Y5tJX1MQlPlqiwlOH1tJY" 

# Spotify API URL for the artist
artist_url = f"https://api.spotify.com/v1/artists/" + artist_id

# Headers for the request, including the Authorization token
headers = {
    "Authorization": "Bearer" + ACCESS_TOKEN
}

# Make the GET request
response = requests.get(artist_url, headers=headers)

# Print the response (artist details)
print(response.json())
