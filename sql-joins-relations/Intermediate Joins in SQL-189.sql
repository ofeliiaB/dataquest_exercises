## 2. Joining Three Tables ##

SELECT t.track_id, t.name as track_name, mt.name AS track_type,  il.unit_price, il.quantity
FROM track t
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
INNER JOIN invoice_line il ON il.track_id = t.track_id
WHERE il.invoice_id = 4;

## 3. Joining More Than Three Tables ##

SELECT
    il.track_id,
    t.name track_name,
    a.name AS artist_name,
    mt.name track_type,
    il.unit_price,
    il.quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
INNER JOIN album ON album.album_id = t.album_id
INNER JOIN artist a ON a.artist_id = album.artist_id
WHERE il.invoice_id = 4;

## 4. Combining Multiple Joins with Subqueries ##

SELECT ta.album, ta.artist, COUNT(*) AS tracks_purchased
FROM invoice_line il
INNER JOIN (
            SELECT t.track_id track_id, 
                   al.title album, 
                   ar.name artist
            FROM album al
            INNER JOIN track t ON t.album_id = al.album_id
            INNER JOIN artist ar ON al.artist_id = ar.artist_id
            ) AS ta ON ta.track_id = il.track_id
GROUP BY ta.album
ORDER BY tracks_purchased DESC
LIMIT 5;

## 5. Recursive Joins ##

SELECT e1.first_name || " " || e1.last_name AS employee_name,
       e1.title AS employee_title,
       e2.first_name || " " || e2.last_name AS supervisor_name,
       e2.title AS supervisor_title
FROM employee e1
LEFT JOIN employee e2 ON e1.reports_to = e2.employee_id 
ORDER BY employee_name;

## 6. Pattern Matching Using Like ##

SELECT first_name, last_name, phone
FROM customer
WHERE first_name LIKE "%BELLE%";

## 7. Generating Columns With The Case Statement ##

SELECT c.first_name || " " || c.last_name AS customer_name,
       i.number_of_purchases,
       i.total_spent,
       CASE 
           WHEN i.total_spent < 40 THEN "small spender"
           WHEN i.total_spent > 100 THEN "big spender"
           ELSE "regular"
           END
           AS customer_category
FROM customer c
INNER JOIN ( 
            SELECT COUNT(*) AS number_of_purchases, SUM(total) total_spent, customer_id
            FROM invoice
            GROUP BY customer_id 
            ) i ON i.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY customer_name;