import sqlite3
import pandas as pd

# Connect to the SQLite database
db_path = "depression_student.db"  # Path to your SQLite database
connection = sqlite3.connect(db_path)

# Function to run a query and display the results
def run_query(query):
    try:
        # Execute the query
        result = pd.read_sql_query(query, connection)
        # Display the results
        print(result)
    except Exception as e:
        print(f"Error executing query: {e}")

# Test your SQL queries one by one
print("1. Count the total number of records:")
run_query("SELECT COUNT(*) AS Total_Records FROM depression_data;")

print("\n3. Find the average academic pressure:")
run_query("SELECT AVG(Academic_Pressure) AS Average_Academic_Pressure FROM depression_data;")

print("\n2. Find the sum of study hours:")
run_query("SELECT SUM(Study_Hours) AS Total_Study_Hours FROM depression_data;")

print("\n4. Filter rows where Dietary Habits = 'Unhealthy':")
run_query("SELECT * FROM depression_data WHERE Dietary_Habits = 'Unhealthy';")

print("\n5. Students who study more than 8 hours:")
run_query("SELECT * FROM depression_data WHERE Study_Hours > 8;")

# Additional Queries
print("\n1. Additional query 1:")
run_query(" SELECT Depression, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM depression_data) AS Percentage FROM depression_data GROUP BY Depression;")

print("\n2. Additional query 2:")
run_query(" SELECT Age, MAX(Academic_Pressure) AS Max_Pressure FROM depression_data GROUP BY Age ORDER BY Max_Pressure DESC;")

# Close the database connection
connection.close()
