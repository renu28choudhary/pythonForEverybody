import sqlite3
import json

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('roster_data.sqlite')
cur = conn.cursor()

# Create tables if they don't exist
cur.execute('''
CREATE TABLE IF NOT EXISTS User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY (user_id) REFERENCES User (id),
    FOREIGN KEY (course_id) REFERENCES Course (id)
)''')

# Open the JSON file
filename = 'roster_data.json'

try:
    with open(filename, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"The file {filename} could not be found!")
    exit()

# Loop through the entries in the loaded JSON
for entry in data:
    name = entry[0]  # First element in the list (name)
    id_number = entry[1]  # Second element in the list (id_number)
    status = entry[2]  # Third element in the list (status)

    # Insert the user data into the User table (if it does not exist)
    cur.execute('''
    INSERT OR IGNORE INTO User (name) 
    VALUES (?)''', (name,))

    # Insert the course data into the Course table (if it does not exist)
    cur.execute('''
    INSERT OR IGNORE INTO Course (title) 
    VALUES (?)''', (id_number,))

    # Get the user_id and course_id that were just inserted or found
    cur.execute('''
    SELECT id FROM User WHERE name = ?''', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('''
    SELECT id FROM Course WHERE title = ?''', (id_number,))
    course_id = cur.fetchone()[0]

    # Insert the member data into the Member table
    cur.execute('''
    INSERT OR REPLACE INTO Member (user_id, course_id, role)
    VALUES (?, ?, ?)''', (user_id, course_id, status))

# Commit changes and close the connection
conn.commit()

# Perform the SQL query and display the result
cur.execute('''
SELECT User.name, Course.title, Member.role 
FROM User JOIN Member JOIN Course
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
''')

rows = cur.fetchall()
for row in rows:
    print(row)

# Perform the final SELECT query
cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X LIMIT 1;
''')

row = cur.fetchone()
print(row[0])

# Close the connection
conn.close()
