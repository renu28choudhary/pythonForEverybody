import urllib.request
from bs4 import BeautifulSoup

# Function to retrieve and follow the links
def follow_links(url, count, position):
    for _ in range(count):
        print('Retrieving:', url)
        # Retrieve the URL and parse the page
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find all anchor tags
        tags = soup('a')
        
        # Get the href attribute of the link at the specified position (1-indexed)
        link = tags[position - 1].get('href', None)
        
        # Follow the link
        url = link
    return tags[position - 1].contents[0]

# Ask for input
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Start the process of following links
last_name = follow_links(url, count, position)

print('The last name retrieved is:', last_name)
