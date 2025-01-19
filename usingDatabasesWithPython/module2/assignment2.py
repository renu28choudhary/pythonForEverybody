import sqlite3
import re

# Connect to SQLite database (this creates the database file)
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Create the Counts table if it doesn't already exist
cur.execute('''
CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)
''')

# Open the mbox.txt file (replace this with the actual path if needed)
file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'mbox.txt'  # Default file

# Open the file and process the lines
with open(file_name, 'r') as file:
    for line in file:
        # Look for lines that start with 'From'
        if line.startswith('From '):
            # Use regex to extract domain name (text after '@')
            words = line.split()
            email = words[1]
            domain = email.split('@')[1]

            # Check if the organization already exists in the database
            cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
            row = cur.fetchone()

            if row is None:
                # Insert new organization if it doesn't exist
                cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
            else:
                # Update the count if it already exists
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

    # Commit the changes after processing all the lines
    conn.commit()

# Fetch and print the top 10 organizations based on email count
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10')

for row in cur:
    print(f"{row[0]} {row[1]}")

# Close the database connection
conn.close()
