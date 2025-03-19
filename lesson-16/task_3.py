import pandas as pd

# Load the datasets
iris_df = pd.read_json("iris.json")
titanic_df = pd.read_excel("titanic.xlsx")
movies_df = pd.read_csv("movie.csv")
flights_df = pd.read_parquet("flights.parquet")

# 1. Iris dataset: Calculate mean, median, and standard deviation for each numerical column
iris_stats = iris_df.describe().loc[['mean', '50%', 'std']]
iris_stats.rename(index={'50%': 'median'}, inplace=True)
print("Iris Dataset Statistics:\n", iris_stats)

# 2. Titanic dataset: Find min, max, and sum of passenger ages
min_age = titanic_df["Age"].min()
max_age = titanic_df["Age"].max()
sum_age = titanic_df["Age"].sum()
print("\nTitanic Passenger Age Statistics:")
print(f"Minimum Age: {min_age}, Maximum Age: {max_age}, Total Age Sum: {sum_age}")

# 3. Movie dataset
# Identify the director with the highest total director_facebook_likes
top_director = movies_df.groupby("director_name")["director_facebook_likes"].sum().idxmax()
print("\nDirector with the Highest Total Facebook Likes:", top_director)

# Find the 5 longest movies and their directors
longest_movies = movies_df.nlargest(5, "duration")[["movie_title", "director_name", "duration"]]
print("\nTop 5 Longest Movies and Their Directors:")
print(longest_movies)

# 4. Flights dataset
# Check for missing values
missing_values = flights_df.isnull().sum()
print("\nMissing Values in Flights Dataset:\n", missing_values)

# Fill missing values in a numerical column with the column’s mean (example: assuming 'air_time' column exists)
if "air_time" in flights_df.columns:
    flights_df["air_time"].fillna(flights_df["air_time"].mean(), inplace=True)
    print("\nMissing values in 'air_time' column filled with mean.")
