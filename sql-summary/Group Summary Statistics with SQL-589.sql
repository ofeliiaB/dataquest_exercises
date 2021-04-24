## 1. Introduction ##

SELECT COUNT(*) AS num_row
FROM invoice
WHERE billing_country = "USA";

## 2. Counting Rows by Group ##

SELECT billing_country, COUNT(*) AS num_row
FROM invoice
GROUP BY billing_country;

## 3. Summary Statistics by Group ##

SELECT invoice_id, SUM(unit_price * quantity) AS total
FROM invoice_line
GROUP BY invoice_id
LIMIT 5;

## 4. Revisiting the Order of Clauses ##

SELECT 3, 6, 2;

## 5. Revisiting the Order of Execution ##

SELECT 3,5,6;

## 6. Summary Statistics by Group Under Conditions ##

SELECT billing_state, COUNT(*) AS num_row, AVG(total) AS avg_sale
FROM invoice
WHERE billing_country = "USA"
GROUP BY billing_state;

## 7. Summary Statistics by Ordered Groups ##

SELECT track_id, COUNT(*) AS num_row, SUM(unit_price*quantity) AS overall_sale
FROM invoice_line
GROUP BY track_id
ORDER BY overall_sale DESC, num_row DESC
LIMIT 5;