import sqlite3
import pandas as pd

# Load the required datasets
iris_df = pd.read_json("iris.json")
titanic_df = pd.read_excel("titanic.xlsx")
flights_df = pd.read_parquet("flights.parquet")
movies_df = pd.read_csv("movie.csv")

# 1. Exploring iris.json
# Rename columns to lowercase
iris_df.columns = iris_df.columns.str.lower()
# Select only 'sepal_length' and 'sepal_width'
iris_selected = iris_df[['sepal_length', 'sepal_width']]
print("Iris Dataset (Selected Columns):")
print(iris_selected.head())

# 2. Exploring titanic.xlsx
# Filter rows where age is above 30
titanic_filtered = titanic_df[titanic_df["Age"] > 30]
print("\nTitanic Passengers Above 30:")
print(titanic_filtered.head())

# Count the number of male and female passengers
gender_counts = titanic_df["Sex"].value_counts()
print("\nTitanic Gender Counts:")
print(gender_counts)

# 3. Exploring Flights parquet file
# Extract 'origin', 'dest', and 'carrier' columns
flights_selected = flights_df[['origin', 'dest', 'carrier']]
print("\nFlights Data (Selected Columns):")
print(flights_selected.head())

# Find the number of unique destinations
unique_destinations = flights_df["dest"].nunique()
print("\nNumber of Unique Destinations:", unique_destinations)

# 4. Exploring movie.csv
# Filter movies with duration > 120 minutes
long_movies = movies_df[movies_df["duration"] > 120]

# Sort by 'director_facebook_likes' in descending order
sorted_movies = long_movies.sort_values(by="director_facebook_likes", ascending=False)
print("\nMovies Longer Than 120 Minutes, Sorted by Director Facebook Likes:")
print(sorted_movies.head())
