import urllib.parse
import urllib.request
import json

# Prompt the user for the location
location = input('Enter location: ')

# Create the API URL with URL encoding for the location
url = 'http://py4e-data.dr-chuck.net/opengeo?' + urllib.parse.urlencode({'q': location})

# Print out the URL being requested
print(f'Retrieving {url}')

# Send the request to the API and retrieve the response
response = urllib.request.urlopen(url)
data = response.read()

# Decode the response into a string format
data_str = data.decode()

# Print the number of characters retrieved
print(f'Retrieved {len(data_str)} characters')

# Try parsing the JSON response
try:
    info = json.loads(data_str)
    
    # Print out the entire JSON for debugging purposes
    print("JSON Response:", json.dumps(info, indent=4))
    
    # Extract the 'plus_code' from the first feature in the 'features' array
    if 'features' in info and len(info['features']) > 0:
        plus_code = info['features'][0]['properties']['plus_code']
        print(f'Plus code: {plus_code}')
    else:
        print("No Plus Code found for the specified location.")
except json.JSONDecodeError as e:
    print("Failed to decode JSON response.")

#Enter location UOC
