import requests
from bs4 import BeautifulSoup
import json
import time

# Base URL for Demoblaze
BASE_URL = "https://www.demoblaze.com/"
LAPTOPS_URL = "https://www.demoblaze.com/#"

# Headers to mimic a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Function to scrape laptop data
def scrape_laptops():
    laptop_data = []
    page = 1
    
    while True:
        print(f"Scraping page {page}...")
        response = requests.get(BASE_URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find all laptops
        items = soup.find_all("div", class_="card-block")
        
        for item in items:
            name = item.find("h4", class_="card-title").text.strip()
            price = item.find("h5").text.strip()
            description = item.find("p", class_="card-text").text.strip()
            
            laptop_data.append({
                "name": name,
                "price": price,
                "description": description
            })
        
        # Check for the next button
        next_button = soup.find("button", id="next2")
        if next_button and "disabled" not in next_button.attrs:
            page += 1
            next_button.click()
            time.sleep(2)  # Wait for page load
        else:
            break  # Exit loop if no next button

    return laptop_data

# Scrape data
laptop_list = scrape_laptops()

# Save data to JSON file
with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptop_list, file, indent=4)

print("Laptop data saved to laptops.json")
