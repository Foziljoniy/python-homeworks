from bs4 import BeautifulSoup

# Load the HTML content
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract the weather forecast table
weather_data = []
rows = soup.find("table").find("tbody").find_all("tr")

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temp = int(cols[1].text.replace("°C", ""))  # Convert temperature to integer
    condition = cols[2].text
    weather_data.append((day, temp, condition))

# Display Weather Data
print("5-Day Weather Forecast:")
for day, temp, condition in weather_data:
    print(f"{day}: {temp}°C, {condition}")

# Find the day with the highest temperature
max_temp_day = max(weather_data, key=lambda x: x[1])
print(f"\nDay with the highest temperature: {max_temp_day[0]} ({max_temp_day[1]}°C)")

# Find all days with "Sunny" condition
sunny_days = [day for day, temp, condition in weather_data if condition == "Sunny"]
print(f"Sunny days: {', '.join(sunny_days)}")

# Calculate the average temperature
average_temp = sum(temp for _, temp, _ in weather_data) / len(weather_data)
print(f"Average temperature for the week: {average_temp:.2f}°C")