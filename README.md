# Using Python to call artist data from Spotify's API
1. Importing the libraries needed
   - requests sends a HTTP request to APIs, a message is sent by the client to a server to request data
   - base64 is needed because client crednetials needs to be sent in a specific format to request an access token
  
2. Defining the Spotify API credentials from my account and creating an app

3. Combining client credentials into a single string in the format client_id:client_secret as API requires this format

4. Converting the string into bytes as this is the format base64 works in

5. 
