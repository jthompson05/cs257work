-- Find earthquakes with magnitude larger than 5 and sort them
SELECT * FROM earthquakes WHERE mag>5 ORDER BY mag DESC;
-- Find most common earthquake location
SELECT place, COUNT(*) AS count FROM earthquakes GROUP BY place ORDER BY count DESC LIMIT 1;
-- Find average earthquake magnitude
SELECT AVG(mag) AS average_magnitude FROM earthquakes;
