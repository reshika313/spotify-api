# Using Python to request access token from Spotify's API using my client credentials
1. Importing the libraries needed
   - requests sends a HTTP request to APIs, a message is sent by the client to a server to request data
   - base64 is needed because client credentials needs to be sent in a specific format to request an access token
  
2. Defining the Spotify API credentials from my account and creating an app

3. Combining client credentials into a single string in the format client_id:client_secret as API requires this format

4. Converting the string into bytes (binary) as this is needed for base64

5. Taking binary data and converting it into ASCII characters (text) to send a request

6. Defining the URL we want to send the POST request to

7. Setting up request headers, authorization header confirms my ID and content type header tells Spotify's servers how to interpret the data you are sending (request body)

8. Setting up request body, sending over the data to Spotify's server (POST request) to receive access token, is in a dictionary format, this format requires no log in

9. Sending over POST request to the specified URL

10. Server sends response from POST request and converting the JSON response into a dictionary, the get() function allows you to access certain values from that dictionary

11. Printing the access token in the terminal
