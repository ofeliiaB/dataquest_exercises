## 1. Introduction ##

SELECT invoice_id, invoice_date, billing_country, total
FROM invoice
LIMIT 3;

## 2. Column Sum ##

SELECT SUM(total) AS overall_sale
FROM invoice;

## 3. Column Average ##

SELECT AVG(total) AS avg_sale
FROM invoice;

## 4. Minimum and Maximum Values in a Numeric Column ##

SELECT MAX(total) AS max_sale
FROM invoice;

## 5. First and Last Values in a Text Column ##

SELECT MAX(billing_country) AS last_billing_country
FROM invoice;

## 6. Counting Rows ##

SELECT COUNT(*) AS num_rows
FROM invoice;

## 7. Counting Rows with Missing Values ##

SELECT COUNT(composer) AS num_composers
FROM track;