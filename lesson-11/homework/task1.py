import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Step 1: Create the Roster table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Step 2: Insert data into Roster table
cursor.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# Step 3: Update Jadzia Dax to Ezri Dax
cursor.execute("""
UPDATE Roster
SET Name = "Ezri Dax"
WHERE Name = "Jadzia Dax"
""")

# Step 4: Retrieve Name and Age of Bajoran characters
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = "Bajoran"
""")
print("Bajoran characters:")
for row in cursor.fetchall():
    print(row)

# Step 5: Delete characters aged over 100 years
cursor.execute("""
DELETE FROM Roster WHERE Age > 100
""")

# Step 6: Add a new column Rank
cursor.execute("""
ALTER TABLE Roster ADD COLUMN Rank TEXT
""")

# Step 7: Update Rank values
cursor.executemany("""
UPDATE Roster SET Rank = ? WHERE Name = ?
""", [
    ("Captain", "Benjamin Sisko"),
    ("Lieutenant", "Ezri Dax"),
    ("Major", "Kira Nerys")
])

# Step 8: Retrieve all characters sorted by Age in descending order
cursor.execute("""
SELECT * FROM Roster ORDER BY Age DESC
""")
print("\nCharacters sorted by Age:")
for row in cursor.fetchall():
    print(row)

# Commit changes and close the connection
conn.commit()
conn.close()
