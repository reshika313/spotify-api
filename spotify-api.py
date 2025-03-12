#1. importing libraries
import requests #library sends requests to APIS and web servers
import base64 #converts binary into text

#2. spotify API credentials
client_id = " "
client_secret = " "

#3. combine credentials into a single string
auth_string = client_id + ":" + client_secret

#4. convert string to bytes
auth_bytes = auth_string.encode("utf-8") #utf- 8 converts string into bytes

#5. encode the bytes in base64
auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

#6. spotify token url
token_url = "https://accounts.spotify.com/api/token"

#7. set up headers for request
headers = {
    "Authorization": "Basic " + auth_base64,
    "Content-Type": "application/x-www-form-urlencoded"
}

#8. set up request body
data = {"grant_type": "client_credentials"}

#9. send request to get access token
response = requests.post(token_url, headers=headers, data=data)

#10. extract access token from response
token_info = response.json()
access_token = token_info.get("access_token")

#11. displaying access token
print("Access Token:", access_token)
