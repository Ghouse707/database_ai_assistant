import sqlite3

## Connect to SQLite
connection = sqlite3.connect("student.db")

## Create cursor
cursor = connection.cursor()

## Create table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""

cursor.execute(table_info)

## Insert records
student_records = [
    ('Ghousr', 'Data Science', 'A', 90),
    ('Sudhanshu', 'Data Science', 'B', 100),
    ('Darius', 'Data Science', 'A', 86),
    ('Shashank', 'DEVOPS', 'A', 50),
    ('Abhi', 'DEVOPS', 'A', 35),
    ('Rahul', 'Cyber Security', 'B', 78),
    ('Priya', 'Artificial Intelligence', 'A', 95),
    ('Aman', 'Machine Learning', 'C', 82),
    ('Sneha', 'Cloud Computing', 'B', 88),
    ('Rohit', 'Web Development', 'A', 76),
    ('Kiran', 'Data Analytics', 'C', 91),
    ('Neha', 'Machine Learning', 'B', 84),
    ('Arjun', 'Cyber Security', 'A', 73),
    ('Pooja', 'Artificial Intelligence', 'A', 98),
    ('Vikram', 'Cloud Computing', 'B', 67),
    ('Anjali', 'Web Development', 'C', 80),
    ('Faizan', 'Data Science', 'B', 92),
    ('Megha', 'DEVOPS', 'A', 58),
    ('Yash', 'Machine Learning', 'A', 89),
    ('Divya', 'Cyber Security', 'B', 77)
]

cursor.executemany(
    "INSERT INTO STUDENT VALUES (?, ?, ?, ?)",
    student_records
)

## Commit changes
connection.commit()

## Display all records
print("The inserted records are:\n")

data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

## Close connection
connection.close()