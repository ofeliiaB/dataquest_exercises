## 3. The With Clause ##

WITH playlist_info AS (
    SELECT p.playlist_id AS playlist_id, 
           p.name AS playlist_name, 
           t.name AS track_name,
           (t.milliseconds / 1000) AS length_seconds
    FROM playlist p
    LEFT JOIN playlist_track pt ON pt.playlist_id = p.playlist_id
    LEFT JOIN track t ON t.track_id = pt.track_id
)

SELECT playlist_id, 
       playlist_name,
       COUNT(track_name) AS number_of_tracks,
       SUM(length_seconds) AS length_seconds
FROM playlist_info
GROUP BY playlist_id, playlist_name
ORDER BY playlist_id

## 4. Creating Views ##

CREATE VIEW chinook.customer_gt_90_dollars AS 
    SELECT
        c.*
    FROM chinook.invoice i
    INNER JOIN chinook.customer c ON i.customer_id = c.customer_id
    GROUP BY 1
    HAVING SUM(i.total) > 90;
SELECT * FROM chinook.customer_gt_90_dollars;

## 5. Combining Rows With Union ##

SELECT * FROM customer_usa
UNION
SELECT * FROM customer_gt_90_dollars;

## 6. Combining Rows Using Intersect and Except ##

/*
SELECT e.first_name || " " || e.last_name AS employee_name,
       COUNT(cg9.customer_id) AS customer_gt_90_dollars
FROM employee e
INNER JOIN customer_gt_90_dollars cg9 ON cg9.support_rep_id = e.employee_id
GROUP BY employee_name
HAVING title = "Sales Support Agent"
ORDER BY employee_name;
*/
WITH customers_usa_gt_90 AS
    (
     SELECT * FROM customer_usa

     INTERSECT

     SELECT * FROM customer_gt_90_dollars
    )

SELECT
    e.first_name || " " || e.last_name employee_name,
    COUNT(c.customer_id) customers_usa_gt_90
FROM employee e
LEFT JOIN customers_usa_gt_90 c ON c.support_rep_id = e.employee_id
WHERE e.title = 'Sales Support Agent'
GROUP BY 1 ORDER BY 1;

## 7. Multiple Named Subqueries ##

WITH 
    india_c AS
    (
        SELECT * FROM customer
        WHERE country = "India"
    ),
    sum_total AS
    (
        SELECT SUM(total) AS sum_total_pc, 
                i.customer_id AS customer_id
        FROM invoice i
        GROUP BY customer_id
    )
        
SELECT india_c.first_name || " " || india_c.last_name AS customer_name,
sum_total.sum_total_pc AS total_purchases
FROM india_c
LEFT JOIN sum_total ON india_c.customer_id = sum_total.customer_id
ORDER BY customer_name;
        

## 8. Challenge: Each Country's Best Customer ##

WITH 
    c_i AS
    (
        SELECT SUM(i.total) AS total_per_c, 
               c.first_name || " " || c.last_name customer_name, 
               c.country AS country
        FROM invoice i
        INNER JOIN customer c ON c.customer_id = i.customer_id
        GROUP BY c.customer_id
        )

SELECT country,
       customer_name,
       MAX(total_per_c) AS total_purchased
FROM c_i
GROUP BY country 