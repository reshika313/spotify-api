import requests #library sends requests to APIS and web servers
import base64 #converts binary into text

#spotify API credentials
client_id = " "
client_secret = " "

#combine credentials into a single string
auth_string = client_id + ":" + client_secret

#convert string to bytes
auth_bytes = auth_string.encode("utf-8")

#encode the bytes in base64
auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

#spotify token url
token_url = "https://accounts.spotify.com/api/token"

#set up headers for request
headers = {
    "Authorization": f"Basic {auth_base64}",
    "Content-Type": "application/x-www-form-urlencoded"
}

#set up request body
data = {"grant_type": "client_credentials"}

#send request to get access token
response = requests.post(token_url, headers=headers, data=data)

#extract access token from response
token_info = response.json()
access_token = token_info.get("access_token")

print("Access Token:", access_token)
