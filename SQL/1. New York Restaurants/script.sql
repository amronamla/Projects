-- Select all columns from the nomnom table
SELECT *
FROM nomnom;

-- Select distinct neighborhoods from nomnom table
SELECT DISTINCT neighborhood
FROM nomnom;

-- Select distinct cuisines from nomnom table
SELECT DISTINCT cuisine
FROM nomnom;

-- Select all columns from nomnom where cuisine is Chinese
SELECT *
FROM nomnom
WHERE cuisine = 'Chinese';

-- Select all columns from nomnom where review is greater than or equal to 4
SELECT *
FROM nomnom
WHERE review >= 4;

-- Select all columns from nomnom where cuisine is Italian and price starts with '$$$'
SELECT *
FROM nomnom
WHERE cuisine = 'Italian'
AND price LIKE '$$$%';

-- Select all columns from nomnom where name contains 'meatball'
SELECT *
FROM nomnom
WHERE name LIKE '%meatball%';

-- Select all columns from nomnom where neighborhood is Midtown, Downtown, or Chinatown
SELECT *
FROM nomnom
WHERE neighborhood = 'Midtown'
OR neighborhood = 'Downtown'
OR neighborhood = 'Chinatown';

-- Select all columns from nomnom where health is NULL
SELECT *
FROM nomnom
WHERE health IS NULL;

-- Select all columns from nomnom, order by review in descending order, and limit to 10 rows
SELECT *
FROM nomnom
ORDER BY review DESC
LIMIT 10;

-- Select all columns from nomnom, and add a calculated column 'rating' based on the review value
SELECT *,
  CASE
    WHEN review > 4.5 THEN 'Extraordinary'
    WHEN review > 4 THEN 'Excellent'
    WHEN review > 3 THEN 'Good'
    WHEN review > 2 THEN 'Fair'
    ELSE 'Poor'
  END AS 'rating'
FROM nomnom;
