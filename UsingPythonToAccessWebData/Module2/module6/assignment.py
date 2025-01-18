import urllib.request
import json

# Prompt the user to enter the URL
url = input('Enter location: ')

# Open the URL and read the data
print(f'Retrieving {url}')
response = urllib.request.urlopen(url)
data = response.read()

# Convert the byte data into a string and then parse the JSON
print(f'Retrieved {len(data)} characters')
info = json.loads(data)

# Initialize the count variable
count = 0
total = 0

# Loop through all comments and sum the counts
for comment in info['comments']:
    count += 1
    total += comment['count']

# Print the results
print(f'Count: {count}')
print(f'Sum: {total}')

#url: http://py4e-data.dr-chuck.net/comments_2157100.json