## 2. Connecting to Postgres ##

import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
conn.close()

## 3. Interacting with the database ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("SELECT * FROM users")
users = cur.fetchall()
conn.close()

## 4. Creating a table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
query = "CREATE TABLE users( id integer PRIMARY KEY, email text, name text, address text);"
cur.execute(query)

## 5. SQL transactions ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("SELECT * FROM users;")

## 6. The commit method ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
query_string = """
    CREATE TABLE users(
        id integer PRIMARY KEY, 
        email text,
        name text,
        address text
    );
"""

cur = conn.cursor()
cur.execute(query_string)
conn.commit()
conn.close()

## 7. Local state and commits ##

import psycopg2
conn1 = psycopg2.connect("dbname=dq user=dq")
cur1 = conn1.cursor()
cur1.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", (1, 'alice@dataquest.io', 'Alice', '99 Fake Street'))

conn2 = psycopg2.connect("dbname=dq user=dq")
cur2 = conn2.cursor()

cur1.execute("SELECT * FROM users;")
view1_before = cur1.fetchall()

cur2.execute("SELECT * FROM users;")
view2_before = cur2.fetchall()

conn1.commit()

cur2.execute("SELECT * FROM users;")
view2_after = cur2.fetchall()

## 9. Inserting data into a table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", (1, "gmail.com", "some_name", "Street"))
conn.commit()
conn.close()

## 10. Copying the data ##

import psycopg2
import csv
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

with open("user_accounts.csv", "r") as f:
    next(f)
    reader = csv.reader(f)
    for row in reader:
        cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", (row[0], row[1], row[2], row[3]))

conn.commit()
conn.close()