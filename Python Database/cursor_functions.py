import sqlite3

connection = sqlite3.connect('StudentDB')

with connection:
    cursor = connection.cursor()
    cursor.execute("SELECT ID, S_NAME,AGE,SEX,CLASS,DIVISION,MARKS FROM STUDENTS")
    # rows = cursor.fetchone()
    # print(rows) # (1, 'Kannan', 14, 'M', 9, 'A', 480.0)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
