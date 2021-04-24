## 1. Connection String ##

import psycopg2
import pprint
conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")
pprint.pprint(conn)

## 2. Creating a User ##

import psycopg2

conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")

cur = conn.cursor()

cur.execute("""
    CREATE USER data_viewer
    WITH SUPERUSER PASSWORD 'secret';

""")

conn.commit()
conn.close()

## 3. The Users Table ##

import psycopg2

conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")

cur = conn.cursor()
cur.execute("SELECT * FROM pg_user;")
users = cur.fetchall()
for i in users:
    print(i)
conn.close()

## 4. User Privileges ##

import psycopg2

conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")
cur = conn.cursor()

cur.execute("REVOKE ALL ON users FROM data_viewer;")

cur.execute("GRANT SELECT ON users TO data_viewer;")

conn.commit()
conn.close()

## 5. Checking User Privileges ##

import psycopg2

conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")
cur = conn.cursor()

cur.execute("SELECT grantor, grantee, privilege_type FROM information_schema.table_privileges WHERE table_name = 'users';")
privileges = cur.fetchall()
for i in privileges:
    print(i)
conn.close()

## 6. Privileges and Superusers ##

import psycopg2
conn = psycopg2.connect(dbname="dq", user="data_viewer", password="secret")
cur = conn.cursor()
cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", 
            (10002, 'alice@dataquest.io', 'Alice', '100, Fake St'))
cur.execute("SELECT * FROM users;")
print(cur.fetchall()[-1])
cur.execute("ALTER USER data_viewer WITH NOSUPERUSER;")
cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", 
            (10002, 'alice@dataquest.io', 'Alice', '100, Fake St'))

## 7. Postgres Groups ##

import psycopg2

conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")
cur = conn.cursor()

cur.execute("""
    CREATE GROUP readonly NOLOGIN;
""")

cur.execute("""
    REVOKE ALL ON users FROM readonly;
""")

cur.execute(""" 
    GRANT SELECT ON users
    TO readonly;
""")

cur.execute("""
    GRANT readonly TO data_viewer;
""")

conn.commit()
conn.close()

## 8. Creating a Read-Write Group ##

import psycopg2

conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")
cur = conn.cursor()

cur.execute("""
    CREATE GROUP readwrite NOLOGIN;
""")

cur.execute("""
    REVOKE ALL ON users FROM readwrite;
""")

cur.execute("""
    GRANT SELECT, INSERT, DELETE, UPDATE ON users
    TO readwrite;
""")

conn.commit()
conn.close()

## 9. Creating a Database ##

import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True

cur = conn.cursor()
cur.execute(" CREATE DATABASE my_database OWNER postgres;")
conn.autocommit = False

## 10. Managing Connection Rights ##

import psycopg2

conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")
cur = conn.cursor()

cur.execute("REVOKE ALL ON DATABASE my_database FROM public;")
cur.execute("REVOKE CONNECT ON DATABASE my_database FROM readonly;")

conn.commit()
conn.close()

## 11. Creating Schemas ##

import psycopg2

conn = psycopg2.connect(dbname="my_database", user="postgres", password="abc123")
cur = conn.cursor()

cur.execute("CREATE SCHEMA my_schema;")

conn.commit()

conn.close()