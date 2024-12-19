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

Output 
    Total_Records
0            503

Query 2: Find the average of a numerical column
SELECT AVG(Academic_Pressure) AS Average_Academic_Pressure FROM depression_data;

Output
    Average_Academic_Pressure
0                   2.998012

Query 3: Find the sum of a numerical column
SELECT SUM(Study_Hours) AS Total_Study_Hours FROM depression_data;

Output
   Total_Study_Hours
0             3215.0

Query 4: Filter records where a column value exceeds a threshold
SELECT * FROM depression_data WHERE Dietary_Habits = 'Unhealthy';

SELECT * FROM depression_data WHERE Study_Hours > 8;
![query5](https://github.com/user-attachments/assets/1e057094-f306-4305-983b-03c3d19511ba)


Additional Queries : 
    1. Find the percentage of students reporting depression:
        SELECT Depression, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM depression_data) AS Percentage
        FROM depression_data
        GROUP BY Depression;

    2. Identify the age group with the highest academic pressure:
        SELECT Age, MAX(Academic_Pressure) AS Max_Pressure
        FROM depression_data
        GROUP BY Age
        ORDER BY Max_Pressure DESC;


