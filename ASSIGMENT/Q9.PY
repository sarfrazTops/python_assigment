9. SQLite3 and PyMySQL (Database Connectors)

Theory:

• Introduction to SQLite3 and PyMySQL for database connectivity.

QLite3 and PyMySQL are two popular Python libraries used for interacting with databases.

SQLite3 is a lightweight, built-in database engine in Python that stores data in a single
file. It is ideal for small-scale applications and quick prototyping.

PyMySQL is a pure Python client for MySQL databases. It enables Python programs to connect
to and interact with MySQL servers.



• Creating and executing SQL queries from Python using these connectors.

Python provides database connectors like SQLite3 and PyMySQL to interact with databases by
executing SQL queries. These connectors act as bridges between Python code and the database
system, allowing the program to create, read, update, and delete records.

Key Steps Involved:
Import the Connector Library

For SQLite: import sqlite3

For MySQL: import pymysql

Establish a Connection

SQLite connects to a local .db file.

PyMySQL connects to a MySQL server using host, user, password, and database name.

Create a Cursor Object

The cursor is used to send SQL commands and fetch results.

Execute SQL Queries

Common queries: CREATE, INSERT, SELECT, UPDATE, DELETE.

Commit Changes (for write operations)

Ensures that insertions and updates are saved.

Close the Connection

Frees resources and ends the session.

Types of SQL Queries You Can Execute:
Data Definition Language (DDL): CREATE TABLE, ALTER, DROP

Data Manipulation Language (DML): INSERT, UPDATE, DELETE

Data Query Language (DQL): SELECT

By using these connectors, Python becomes a powerful tool for backend development,
data management, and automation tasks involving relational databases.


Lab:

• Write a Python program to connect to an SQLite3 database, create a table, insert data, and
fetch data.

import sqlite3


conn = sqlite3.connect('students.db')


cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
""")


cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Alice", 20, "A"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Bob", 22, "B"))


conn.commit()


cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)


conn.close()




Practical Examples: 21) Write a Python program to create a database and a table using SQLite3.



import sqlite3


conn = sqlite3.connect("mydatabase.db")


cursor = conn.cursor()


cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT ,
    age INTEGER,
    
)
""")


conn.commit()
conn.close()

print("Database and table created successfully!")

22) Write a Python program to insert data into an SQLite3 database and fetch it.

import sqlite3


conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")

cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ("Alice", 25, "alice@example.com"))
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ("Bob", 30, "bob@example.com"))


conn.commit()


cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("User Data from Database:")
for row in rows:
    print(row)


conn.close()


