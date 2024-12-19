-- Query 1: Count the total number of records in the dataset
SELECT COUNT(*) AS Total_Records FROM depression_data;

-- Query 2: Find the sum of a numerical column
SELECT SUM(Study_Hours) AS Total_Study_Hours FROM depression_data;

-- Query 3: Find the average of a numerical column
SELECT AVG(Academic_Pressure) AS Average_Academic_Pressure FROM depression_data;

-- Query 4: Filter records where a column value exceeds a threshold
SELECT * FROM depression_data WHERE Dietary_Habits = 'Unhealthy';
SELECT * FROM depression_data WHERE Study_Hours > 8;

--  Additional Examples (Optional)
-- Find the percentage of students reporting depression:
SELECT Depression, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM depression_data) AS Percentage
FROM depression_data
GROUP BY Depression;

-- Identify the age group with the highest academic pressure:
SELECT Age, MAX(Academic_Pressure) AS Max_Pressure
FROM depression_data
GROUP BY Age
ORDER BY Max_Pressure DESC;

