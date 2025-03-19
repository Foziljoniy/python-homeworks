import sqlite3
import pandas as pd

# 1. Reading the customers table from chinook.db
conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print("Customers Table (First 10 Rows):")
print(customers_df.head(10))
conn.close()

# 2. Loading iris.json
iris_df = pd.read_json("iris.json")
print("\nIris Dataset Shape:", iris_df.shape)
print("Column Names:", iris_df.columns.tolist())

# 3. Loading titanic.xlsx
titanic_df = pd.read_excel("titanic.xlsx")
print("\nTitanic Dataset (First 5 Rows):")
print(titanic_df.head())

# 4. Reading Flights parquet file
flights_df = pd.read_parquet("flights.parquet")
print("\nFlights Dataset Info:")
print(flights_df.info())

# 5. Loading movie.csv
movies_df = pd.read_csv("movie.csv")
print("\nRandom Sample of 10 Rows from Movies Dataset:")
print(movies_df.sample(10))
