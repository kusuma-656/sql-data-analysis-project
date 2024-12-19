# SQL Data Analysis on a Local Database

## Description
This project demonstrates SQL data analysis on a local SQLite database. The dataset used is the **Student Depression Dataset** from Kaggle, which includes information on students' study habits, dietary habits, depression status, and academic pressure. SQL queries are written to analyze and filter data based on various conditions, such as counting records, summing study hours, averaging values, and identifying patterns like the percentage of students reporting depression.

## Database Used
- **SQLite**: A lightweight, serverless relational database used for this project.

## Dataset
- **Dataset Name**: Student Depression Dataset
- **Source**: [Kaggle](https://www.kaggle.com/datasets)
- **Description**: The dataset contains information about students' study hours, dietary habits, academic pressure, and depression status.

## Installation Steps and Procedure

1. **Install SQLite**:
   - Download SQLite from the [official website](https://www.sqlite.org/download.html).
   - Install and set up SQLite on your local machine.

2. **Download the Dataset**:
   - Download the Student Depression Dataset from [Kaggle](https://www.kaggle.com/datasets).
   - Save it in CSV format to your local machine.

3. **Import the Dataset to SQLite**:
   - Open SQLite command-line tool (or use an SQLite GUI like DB Browser for SQLite).
   - Create a new SQLite database by running the following command:
     ```bash
     sqlite3 depression.db
     ```
   - Create a table based on the structure of the dataset.
   - Import the dataset into the SQLite database using the command:
     ```bash
     .mode csv
     .import /path/to/your/data.csv depression_data
     ```

## Running Queries

Here are the SQL queries used for data analysis:

### Query 1: Count the total number of records in the dataset
```sql
SELECT COUNT(*) AS Total_Records FROM depression_data;

Result:
Screenshot: results/query1,query2,query3.png
CSV: results/query1_results.csv

### Query 2: Find the sum of study hours:
SELECT SUM(Study_Hours) AS Total_Study_Hours FROM depression_data;

Result:
Screenshot: results/query1,query2,query3.png
CSV: results/query3_result.csv

### Query 3: Find the average of a numerical column
SELECT AVG(Academic_Pressure) AS Average_Academic_Pressure FROM depression_data;

Result:
Screenshot: results/query1,query2,query3.png
CSV: results/query2_result.csv

### Query 4: Filter records where a column value exceeds a threshold
SELECT * FROM depression_data WHERE Dietary_Habits = 'Unhealthy';

Result:
Screenshot: results/query4.png
CSV: results/query4_results.csv

SELECT * FROM depression_data WHERE Study_Hours > 8;

Result:
Screenshot: results/query4.png
CSV: results/condition_based_results.csv

### Additional Examples (Optional)
Find the percentage of students reporting depression:

SELECT Depression, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM depression_data) AS Percentage
FROM depression_data
GROUP BY Depression;

Identify the age group with the highest academic pressure:
SELECT Age, MAX(Academic_Pressure) AS Max_Pressure
FROM depression_data
GROUP BY Age
ORDER BY Max_Pressure DESC;


5. Commit and Push to GitHub
After you’ve documented your queries and results:
- Commit all files (i.e., `queries.sql`, `README.md`, `results/` folder) to your local Git repository.
- Push the repository to GitHub.

```bash
git add .
git commit -m "Add SQL queries and results"
git push origin main
