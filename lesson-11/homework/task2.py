import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Step 1: Create the Books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# Step 2: Insert data into Books table
cursor.executemany("""
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

# Step 3: Update Year_Published of 1984 to 1950
cursor.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = "1984"
""")

# Step 4: Retrieve Title and Author of Dystopian books
cursor.execute("""
SELECT Title, Author FROM Books WHERE Genre = "Dystopian"
""")
print("Dystopian books:")
for row in cursor.fetchall():
    print(row)

# Step 5: Delete books published before 1950
cursor.execute("""
DELETE FROM Books WHERE Year_Published < 1950
""")

# Step 6: Add a new column Rating
cursor.execute("""
ALTER TABLE Books ADD COLUMN Rating REAL
""")

# Step 7: Update Rating values
cursor.executemany("""
UPDATE Books SET Rating = ? WHERE Title = ?
""", [
    (4.8, "To Kill a Mockingbird"),
    (4.7, "1984"),
    (4.5, "The Great Gatsby")
])

# Step 8: Retrieve all books sorted by Year_Published in ascending order
cursor.execute("""
SELECT * FROM Books ORDER BY Year_Published ASC
""")
print("\nBooks sorted by Year Published:")
for row in cursor.fetchall():
    print(row)

# Commit changes and close the connection
conn.commit()
conn.close()
