# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
 
 # Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
 # Prompt the user to enter a file name and provide a default
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

# Open the file for reading
handle = open(fname)

# Dictionary to store counts of messages per hour
hour_counts = {}

# Loop through the lines in the file
for line in handle:
    # Look for lines starting with 'From '
    if line.startswith("From "):
        words = line.split()  # Split the line into words
        time = words[5]       # Extract the time (6th element)
        hour = time.split(':')[0]  # Split the time and get the hour
        # Increment the count for the hour
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Close the file
handle.close()

# Sort the dictionary by hour and print the sorted counts
for hour, count in sorted(hour_counts.items()):
    print(hour, count)
