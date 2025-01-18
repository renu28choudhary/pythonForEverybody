import socket

# Create a socket object for connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at 'data.pr4e.org' on port 80 (HTTP)
mysock.connect(('data.pr4e.org', 80))

# Modify the request to point to the new URL
cmd = 'GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()

# Send the GET request
mysock.send(cmd)

# Initialize a variable to store the server's response
response = b""

# Loop to receive the response data
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    response += data

# Close the socket connection
mysock.close()

# Decode the response from bytes to a string
response_text = response.decode()

# Split the response into headers and body
headers, body = response_text.split('\r\n\r\n', 1)

# Print the headers and body
print("Headers:\n", headers)
print("\nBody:\n", body)
