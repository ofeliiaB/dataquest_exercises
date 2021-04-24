## 3. Connecting to the Database ##

import sqlite3

conn = sqlite3.connect("jobs.db")

## 6. Creating a Cursor and Running a Query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select Major from recent_grads;"
cursor.execute(query)
majors = cursor.fetchall()
print(majors[0:3])

## 8. Fetching a Specific Number of Results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
query = "select Major, Major_category FROM recent_grads;"
cursor.execute(query)
five_results = cursor.fetchmany(5)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

import sqlite3

conn = sqlite3.connect("jobs2.db")
cursor = conn.cursor()

query = "SELECT Major FROM recent_grads ORDER BY 1 DESC;"
cursor.execute(query)
reverse_alphabetical = cursor.fetchall()
print(reverse_alphabetical)
conn.close()