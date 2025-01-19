import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Drop existing tables if they exist
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;       -- Added drop for Genre table
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE          -- This column will hold the genre name
);

CREATE TABLE Album (
    id  INTEGER PRIMARY KEY,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER PRIMARY KEY,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,       -- Added reference to Genre table
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Open the CSV file
handle = open('tracks.csv')

# Process each line in the CSV
for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 6:
        continue

    # Extract data from each line
    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]  # Assuming there's a genre column in the CSV (position 6)

    print(name, artist, album, genre, count, rating, length)

    # Insert artist if it doesn't exist
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', (artist,))

    # Get the artist_id for the album
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    # Insert genre if it doesn't exist
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', (genre,))
    
    # Get the genre_id for the track
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    # Insert album if it doesn't exist
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', (album, artist_id))

    # Get the album_id for the track
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    # Insert track details with the new genre_id
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        (name, album_id, genre_id, length, rating, count))

    # Commit changes to the database
    conn.commit()

# Close the file and connection
handle.close()
conn.close()
