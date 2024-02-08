import sqlite3

connection = sqlite3.connect('StudentDB')

cursor = connection.cursor()

for row in cursor.execute("SELECT ID, S_NAME,AGE,SEX,CLASS,DIVISION,MARKS FROM STUDENTS"):
    print(f"ID = {row[0]}")
    print(f"NAME = {row[1]}")
    print(f"AGE = {row[2]}")
    print(f"SEX = {row[3]}")
    print(f"CLASS = {row[4]}")
    print(f"DIVISION = {row[5]}")
    print(f"MARKS = {row[6]}\n")

connection.commit()
connection.close()
