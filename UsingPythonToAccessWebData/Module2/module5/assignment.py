import urllib.request
import xml.etree.ElementTree as ET

# Prompt the user for the URL
url = input("Enter location: ")

# Open the URL and read the XML data
response = urllib.request.urlopen(url)
xml_data = response.read()

# Parse the XML data
tree = ET.ElementTree(ET.fromstring(xml_data))

# Find all 'count' tags in the XML using XPath
counts = tree.findall('.//count')

# Calculate the sum of the comment counts
sum_counts = sum(int(count.text) for count in counts)

# Print the result
print(f"Count: {len(counts)}")
print(f"Sum: {sum_counts}")
 #url http://py4e-data.dr-chuck.net/comments_2157099.xml