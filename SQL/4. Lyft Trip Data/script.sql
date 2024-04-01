-- Select all columns from the trips table
SELECT * FROM trips;

-- Select all columns from the riders table
SELECT * FROM riders;

-- Select all columns from the cars table
SELECT * FROM cars;

-- Select all columns from trips and matching rows from riders based on rider_id
SELECT *
FROM trips
LEFT JOIN riders
ON trips.rider_id = riders.id;

-- Select all columns from trips and matching rows from cars based on car_id
SELECT *
FROM trips
JOIN cars
ON trips.car_id = cars.id;

-- Combine rows from riders and riders2 tables, removing duplicates
SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

-- Calculate the average cost of trips and round to 2 decimal places
SELECT ROUND(AVG(cost), 2) AS 'average cost'
FROM trips;

-- Select first and last names from riders where total_trips is less than 500,
-- combined with first and last names from riders2 where total_trips is less than 500
SELECT first, last
FROM riders
WHERE total_trips < 500
UNION
SELECT first, last
FROM riders2
WHERE total_trips < 500;

-- Count the number of cars with status 'active'
SELECT COUNT(*)
FROM cars
WHERE status = 'active';

-- Select all columns from cars, order by trips_completed in descending order, and limit to 2 rows
SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;
