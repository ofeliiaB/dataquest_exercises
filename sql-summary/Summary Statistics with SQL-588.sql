## 1. Introduction ##

SELECT name, album_id, milliseconds
FROM track
WHERE unit_price >=1;

## 2. Using Several Statistics in a Column ##

SELECT MIN(milliseconds) AS min_runtime,
MAX(milliseconds) AS max_runtime
FROM track;

## 3. Using Aggregate Functions with Computed Columns ##

SELECT AVG(milliseconds/1000.0/60) as avg_runtime_minutes,
AVG(bytes/1024.0/1024) as avg_size_megabyte
FROM track;

## 4. Combining Aggregate and Scalar Functions ##

SELECT AVG(milliseconds / 1000.0 / 60) AS avg_runtime_minutes,
ROUND(AVG(milliseconds / 1000.0 / 60), 2) AS avg_runtime_minutes_rounded
FROM track;

## 5. Combining Aggregate Functions with Arithmetic Operators ##

SELECT AVG(milliseconds) AS avg_runtime,
SUM(milliseconds) *1.0 / COUNT(milliseconds) as another_avg_runtime
FROM track;

## 6. Summary Statistics Under a Condition ##

SELECT SUM(milliseconds/1000.0/60) as total_runtime_minutes
FROM track
WHERE unit_price = 1.99;