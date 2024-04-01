-- Count the total number of companies in the startups table
SELECT COUNT(*) AS 'total number of companies'
FROM startups;

-- Calculate the total value of companies (sum of valuations) in the startups table
SELECT SUM(valuation) AS 'total value of companies'
FROM startups;

-- Find the highest amount raised by a startup in the startups table
SELECT MAX(raised) AS 'highest amount raised by a startup'
FROM startups;

-- Find the highest amount raised during Seed stage in the startups table
SELECT MAX(raised) AS 'highest amount raised during Seed stage'
FROM startups
WHERE stage = 'Seed';

-- Find the founding year of the oldest company in the startups table
SELECT MIN(founded) AS 'oldest company'
FROM startups;

-- Calculate the average valuation for each category, rounding to 2 decimal places
SELECT category, ROUND(AVG(valuation), 2) AS 'average valuation'
FROM startups
GROUP BY 1
ORDER BY 2 DESC;

-- Count the number of companies for each category, only include categories with more than 3 companies
SELECT category, COUNT(*) AS 'number of companies'
FROM startups
GROUP BY 1
HAVING COUNT(*) > 3;

-- Calculate the average size of employees for each location, only include locations with an average size greater than 500
SELECT location, AVG(employees) AS 'average size of employees'
FROM startups
GROUP BY 1
HAVING AVG(employees) > 500;
