##Task1


import sqlite3

DB_NAME = 'roster.db'

def connect_db():
    """Connect to the SQLite database and return the connection and cursor."""
    conn = sqlite3.connect(DB_NAME)
    return conn, conn.cursor()

def initialize_database(cursor):
    """Create the Roster table if it doesn't exist."""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT PRIMARY KEY,
        Species TEXT,
        Age INTEGER
    )
    """)

def insert_initial_data(cursor):
    """Insert initial data into the Roster table."""
    characters = [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ]
    for name, species, age in characters:
        cursor.execute("""
        INSERT OR IGNORE INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
        """, (name, species, age))

def update_character_name(cursor, old_name, new_name):
    """Update a character's name."""
    cursor.execute("""
    UPDATE Roster SET Name = ? WHERE Name = ?
    """, (new_name, old_name))

def query_bajoran_characters(cursor):
    """Display Name and Age of all Bajoran characters."""
    print("\n Bajoran Characters:")
    cursor.execute('SELECT Name, Age FROM Roster WHERE Species = ?', ('Bajoran',))
    for name, age in cursor.fetchall():
        print(f" - {name}, Age: {age}")

def delete_old_characters(cursor, age_limit=100):
    """Delete characters older than the specified age limit."""
    cursor.execute('DELETE FROM Roster WHERE Age > ?', (age_limit,))

def add_rank_column(cursor):
    """Add the Rank column to the table if it does not already exist."""
    try:
        cursor.execute('ALTER TABLE Roster ADD COLUMN Rank TEXT')
    except sqlite3.OperationalError:
        pass  

def update_ranks(cursor):
    """Update the ranks of characters."""
    ranks = {
        'Benjamin Sisko': 'Captain',
        'Ezri Dax': 'Lieutenant',
        'Kira Nerys': 'Major'
    }
    for name, rank in ranks.items():
        cursor.execute("""
        UPDATE Roster SET Rank = ? WHERE Name = ?
        """, (rank, name))

def display_sorted_characters(cursor):
    """Display all characters sorted by Age in descending order."""
    print("\n Characters Sorted by Age (Descending):")
    cursor.execute('SELECT Name, Species, Age, Rank FROM Roster ORDER BY Age DESC')
    for name, species, age, rank in cursor.fetchall():
        print(f" - {name} ({species}) - Age: {age}, Rank: {rank}")

def main():
    conn, cursor = connect_db()
    try:
        initialize_database(cursor)
        insert_initial_data(cursor)
        update_character_name(cursor, 'Jadzia Dax', 'Ezri Dax')
        query_bajoran_characters(cursor)
        delete_old_characters(cursor)
        add_rank_column(cursor)
        update_ranks(cursor)
        display_sorted_characters(cursor)
        conn.commit()
    except Exception as e:
        print(f" Error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()


##Task2



import sqlite3

DB_NAME = 'library.db'

def connect_db():
    """Connect to the SQLite database and return the connection and cursor."""
    conn = sqlite3.connect(DB_NAME)
    return conn, conn.cursor()

def initialize_database(cursor):
    """Create the Books table if it doesn't exist."""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT PRIMARY KEY,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
    """)

def insert_initial_data(cursor):
    """Insert initial data into the Books table."""
    books = [
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
        ('1984', 'George Orwell', 1949, 'Dystopian'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
    ]
    for title, author, year, genre in books:
        cursor.execute("""
        INSERT OR IGNORE INTO Books (Title, Author, Year_Published, Genre)
        VALUES (?, ?, ?, ?)
        """, (title, author, year, genre))

def update_year_published(cursor):
    """Update the publication year of '1984' to 1950."""
    cursor.execute("""
    UPDATE Books SET Year_Published = ? WHERE Title = ?
    """, (1950, '1984'))

def query_dystopian_books(cursor):
    """Display Title and Author of all Dystopian books."""
    print("\n Dystopian Books:")
    cursor.execute('SELECT Title, Author FROM Books WHERE Genre = ?', ('Dystopian',))
    for title, author in cursor.fetchall():
        print(f" - {title} by {author}")

def delete_old_books(cursor, year_limit=1950):
    """Delete books published before the given year."""
    cursor.execute('DELETE FROM Books WHERE Year_Published < ?', (year_limit,))

def add_rating_column(cursor):
    """Add the Rating column to the table if not already added."""
    try:
        cursor.execute('ALTER TABLE Books ADD COLUMN Rating REAL')
    except sqlite3.OperationalError:
        pass  

def update_ratings(cursor):
    """Update book ratings."""
    ratings = {
        'To Kill a Mockingbird': 4.8,
        '1984': 4.7,
        'The Great Gatsby': 4.5
    }
    for title, rating in ratings.items():
        cursor.execute("""
        UPDATE Books SET Rating = ? WHERE Title = ?
        """, (rating, title))

def display_books_sorted(cursor):
    """Display all books sorted by publication year (ascending)."""
    print("\n Books Sorted by Year Published:")
    cursor.execute('SELECT Title, Author, Year_Published, Genre, Rating FROM Books ORDER BY Year_Published ASC')
    for title, author, year, genre, rating in cursor.fetchall():
        print(f" - {title} ({year}) by {author} - Genre: {genre}, Rating: {rating}")

def main():
    conn, cursor = connect_db()
    try:
        initialize_database(cursor)
        insert_initial_data(cursor)
        update_year_published(cursor)
        query_dystopian_books(cursor)
        delete_old_books(cursor)
        add_rating_column(cursor)
        update_ratings(cursor)
        display_books_sorted(cursor)
        conn.commit()
    except Exception as e:
        print(f" Error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
