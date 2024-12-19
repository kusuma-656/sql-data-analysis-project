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

## Project Requirements
- SQLite (for the database)
- Python (optional for running queries or scripts)
- DB Browser for SQLite (optional for GUI-based interaction with the database)

## Future Improvements
- Implement more advanced queries to explore relationships between depression and other factors.
- Visualize the results using Python libraries like `matplotlib` or `seaborn`.

## Acknowledgments
- Dataset: [Student Depression Dataset from Kaggle](https://www.kaggle.com/datasets)
- Special thanks to the Kaggle community for making the dataset available.

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

Output
    Gender  Age  Academic_Pressure  Study_Satisfaction     Sleep_Duration  ... Suicidal_Thoughts Study_Hours  Financial_Stress  Family_History_Mental_Illness Depression
0     Male   25                1.0                 3.0          5-6 hours  ...               Yes          10                 4                             No        Yes
1     Male   23                1.0                 4.0  More than 8 hours  ...               Yes           7                 2                            Yes         No
2     Male   19                4.0                 4.0          5-6 hours  ...               Yes           1                 4                            Yes        Yes
3     Male   33                4.0                 3.0  Less than 5 hours  ...               Yes          10                 1                             No        Yes
4     Male   24                2.0                 1.0          7-8 hours  ...               Yes          11                 5                             No        Yes
..     ...  ...                ...                 ...                ...  ...               ...         ...               ...                            ...        ...
164   Male   34                4.0                 1.0          7-8 hours  ...               Yes          11                 5                             No        Yes
165   Male   29                3.0                 1.0          7-8 hours  ...               Yes           9                 3                            Yes        Yes
166   Male   26                5.0                 2.0  More than 8 hours  ...                No           8                 3                             No        Yes
167   Male   24                2.0                 1.0  Less than 5 hours  ...               Yes           8                 5                             No        Yes
168   Male   18                5.0                 3.0  More than 8 hours  ...                No           6                 2                            Yes        Yes

[169 rows x 11 columns]

SELECT * FROM depression_data WHERE Study_Hours > 8;

Output
    Gender  Age  Academic_Pressure  Study_Satisfaction  ...  Study_Hours  Financial_Stress     Family_History_Mental_Illness  Depression
0    Gender  Age  Academic Pressure  Study Satisfaction  ...  Study Hours  Financial Stress  Family History of Mental Illness  Depression
1      Male   28                2.0                 4.0  ...            9                 2                               Yes          No
2      Male   25                1.0                 3.0  ...           10                 4                                No         Yes
3    Female   33                1.0                 4.0  ...           10                 3                                No          No
4      Male   33                4.0                 3.0  ...           10                 1                                No         Yes
..      ...  ...                ...                 ...  ...          ...               ...                               ...         ...
169    Male   20                3.0                 4.0  ...            9                 5                               Yes         Yes
170  Female   27                2.0                 3.0  ...           11                 2                               Yes          No
171  Female   21                5.0                 1.0  ...           12                 3                                No         Yes
172    Male   34                4.0                 1.0  ...           11                 5                                No         Yes
173    Male   29                3.0                 1.0  ...            9                 3                               Yes         Yes

[174 rows x 11 columns]


Additional Queries : 
    1. Find the percentage of students reporting depression:
        SELECT Depression, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM depression_data) AS Percentage
        FROM depression_data
        GROUP BY Depression;

      Output
         Depression  Percentage
      0  Depression    0.198807
      1          No   49.701789
      2         Yes   50.099404

    2. Identify the age group with the highest academic pressure:
        SELECT Age, MAX(Academic_Pressure) AS Max_Pressure
        FROM depression_data
        GROUP BY Age
        ORDER BY Max_Pressure DESC;

      Output
         Age       Max_Pressure
      0   Age  Academic Pressure
      1    34                5.0
      2    33                5.0
      3    32                5.0
      4    31                5.0
      5    30                5.0
      6    29                5.0
      7    28                5.0
      8    27                5.0
      9    26                5.0
      10   25                5.0
      11   24                5.0
      12   23                5.0
      13   22                5.0
      14   21                5.0
      15   20                5.0
      16   19                5.0






