-- Select the title and score from hacker_news, ordered by score in descending order, and limit to 5 rows
SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

-- Calculate the sum of scores in the hacker_news table
SELECT SUM(score)
FROM hacker_news;

-- Select user and sum of score for users with a total score greater than 200, grouped by user
SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200;

-- Calculate the percentage of the sum of given values relative to 6366
SELECT (517 + 309 + 304 + 282) / 6366.0 * 100;

-- Count the number of stories for each user where the URL contains a specific pattern
SELECT user, url, COUNT(*) 'video count'
FROM hacker_news
GROUP BY user
HAVING url LIKE '%www.youtube.com/watch?v=dQw4w9WgXcQ%';

-- Categorize sources based on the URL and count the number of stories for each category
SELECT
  CASE
    WHEN url LIKE '%github.com%' THEN 'GitHub'
    WHEN url LIKE '%medium.com%' THEN 'Medium'
    WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
    ELSE 'Other'
  END AS 'Source',
  COUNT(*) AS 'number of stories'
FROM hacker_news
GROUP BY 1;

-- Group stories by hour of the timestamp, calculate the average score and count for each hour
SELECT
  strftime('%H', timestamp) AS 'hour',
  ROUND(AVG(score)) AS 'average score',
  COUNT(*) AS 'story count'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1;
