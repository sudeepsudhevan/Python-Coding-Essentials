import sqlite3

connection = sqlite3.connect('StudentDB')

cursor = connection.cursor()

sql = "UPDATE STUDENTS SET AGE = AGE + 1 WHERE SEX = ('M')"

try:
    cursor.execute(sql)
    connection.commit()

except:
    connection.rollback()

print("Table below shows the students details with updated age")

try:
    cursor.execute("SELECT ID, S_NAME,AGE,SEX,CLASS,DIVISION,MARKS FROM STUDENTS")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except:
    connection.rollback()
connection.close() 
