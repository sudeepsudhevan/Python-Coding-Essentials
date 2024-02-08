# Creating a Table
import sqlite3

db = sqlite3.connect('StudentDB')

cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS STUDENTS')

sql = """CREATE TABLE STUDENTS(
ID PRIMARY KEY,
S_NAME CHAR(20) NOT NULL,
AGE INT, SEX CHAR(1),
CLASS INT,
DIVISION CHAR(1),
MARKS FLOAT
)
"""

cursor.execute(sql)

db.close()
