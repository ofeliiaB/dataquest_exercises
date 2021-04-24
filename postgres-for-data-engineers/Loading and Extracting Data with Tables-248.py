## 1. The Mogrify Method ##

from datetime import date
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
game_data = (52499790661213, 'Amazing', 'LittleBigPlanet PS Vita', '/games/littlebigplanet-vita/vita-98907', 'PlayStation Vita', 9.0, 'Platformer', 'y', date(2012, 12, 9))
mogrified_values = cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", game_data)
print(mogrified_values)

## 2. The Connection Encoding ##

from datetime import date
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
game_data = (52499790661213, 'Amazing', 'LittleBigPlanet PS Vita', '/games/littlebigplanet-vita/vita-98907', 'PlayStation Vita', 9.0, 'Platformer', 'y', date(2012, 12, 9))

conn_encoding = conn.encoding
print(conn_encoding)
mogrified_values = cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", game_data)
mogrified_values_decoded = mogrified_values.decode(conn_encoding)
print(mogrified_values_decoded)

## 3. Inserting with Mogrify ##

import csv
import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
rows = []
with open("ign.csv", 'r') as f:
    next(f)
    reader = csv.reader(f)
    rows = [row for row in reader]
    mogrified_rows = [cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", row) for row in rows]
    decoded_rows = [row.decode(conn.encoding) for row in mogrified_rows]
    insert_string = ",".join(decoded_rows)
    cur.execute("INSERT INTO ign_reviews VALUES "+ insert_string +";")
    conn.commit()
    conn.close()
    

## 4. Postgres Copy Method ##

import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
with open("ign.csv", "r") as f:
    next(f)
    cur.copy_from(f, "ign_reviews", sep=",")
conn.commit()
conn.close()

## 5. The COPY Statement ##

import csv
import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

with open("ign.csv", "r") as f:
    cur.copy_expert("COPY ign_reviews FROM STDIN WITH CSV HEADER", f)
conn.commit()
conn.close()

## 6. Which method is faster? ##

import csv
import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Multiple single insert statements
def multiple_inserts():
    with open("ign.csv", "r") as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO ign_reviews VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", row)
    conn.rollback()
        
# Multiple mogrify insert
def mogrified_insert():
    with open("ign.csv", "r") as f:
        next(f)
        reader = csv.reader(f)
        mogrified = [ 
            cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", row).decode(conn.encoding)
            for row in reader
        ] 
        mogrified_values = ",".join(mogrified) 
        cur.execute("INSERT INTO ign_reviews VALUES " + mogrified_values + ";")
    conn.rollback()
    
# Copy expert method
def copy_expert():
    with open("ign.csv", "r") as f:
        cur.copy_expert("COPY ign_reviews FROM STDIN WITH CSV HEADER;", f)
    conn.rollback()

import timeit
time_multiple_inserts = timeit.timeit(multiple_inserts, number=1)
time_mogrified_insert = timeit.timeit(mogrified_insert, number=1)
time_copy_expert = timeit.timeit(copy_expert, number=1)

print(time_multiple_inserts)
print(time_mogrified_insert)
print(time_copy_expert)

## 7. Extracting Table to CSV File ##

import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

with open("ign_copy.csv", "w") as f:
    cur.copy_expert("COPY ign_reviews TO STDOUT WITH CSV  HEADER", f)

conn.commit()
conn.close()

## 8. Making a Copy of a Table ##

import psycopg2
# the query for you to create the empty table copy
create_string = """
CREATE TABLE ign_reviews_copy (
    id bigint PRIMARY KEY,
    score_phrase evaluation_enum,
    title varchar(200),
    url varchar(200),
    platform platform_enum,
    score decimal(3, 1),
    genre genre_enum,
    editors_choice boolean,
    release_date date
);
"""

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

with open("temp.csv", "w") as f:
    cur.copy_expert("COPY ign_reviews TO STDOUT WITH CSV  HEADER", f)
cur.execute(create_string)

with open("temp.csv", "r") as f:
     cur.copy_expert("COPY ign_reviews_copy FROM STDIN WITH CSV HEADER", f)
conn.commit()
conn.close()

## 9. Copy with Insert and Select ##

import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

cur.execute("CREATE TABLE ign_restricted (id bigint PRIMARY KEY, title varchar(200), release_date date); ")

cur.execute(""" 
    INSERT INTO ign_restricted (id, title, release_date)
    SELECT id, title, release_date
    FROM ign_reviews;
""")

conn.commit()
conn.close()