import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

# Database setup
db_name = "jobs.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        apply_link TEXT,
        UNIQUE(job_title, company, location)
    )
''')
conn.commit()

# Scrape job listings
url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

job_listings = soup.find_all("div", class_="card-content")

for job in job_listings:
    title = job.find("h2", class_="title is-5").text.strip()
    company = job.find("h3", class_="subtitle is-6 company").text.strip()
    location = job.find("p", class_="location").text.strip()
    description = job.find("div", class_="content").text.strip()
    apply_link = job.find("a", text="Apply")['href']
    
    cursor.execute('''
        INSERT INTO jobs (job_title, company, location, description, apply_link)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(job_title, company, location) 
        DO UPDATE SET description=excluded.description, apply_link=excluded.apply_link
    ''', (title, company, location, description, apply_link))

conn.commit()

# Filtering function
def filter_jobs(location=None, company=None):
    query = "SELECT job_title, company, location, description, apply_link FROM jobs WHERE 1=1"
    params = []
    
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    
    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")
    
    cursor.execute(query, params)
    return cursor.fetchall()

# Export function
def export_to_csv(filename, location=None, company=None):
    jobs = filter_jobs(location, company)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Description", "Apply Link"])
        writer.writerows(jobs)
    print(f"Data exported to {filename}")

# Example usage
export_to_csv("filtered_jobs.csv", location="Remote")

# Close database connection
conn.close()