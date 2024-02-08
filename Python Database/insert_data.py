import sqlite3

connection = sqlite3.connect('StudentDB')

cursor = connection.cursor()

cursor.execute("INSERT INTO STUDENTS(ID,S_NAME,AGE,SEX,CLASS,DIVISION,MARKS) VALUES (1,'Kannan',14,'M',9,'A',480)")
cursor.execute("INSERT INTO STUDENTS(ID,S_NAME,AGE,SEX,CLASS,DIVISION,MARKS) VALUES (2,'Erin',14,'F',9,'C',465)")
cursor.execute("INSERT INTO STUDENTS(ID,S_NAME,AGE,SEX,CLASS,DIVISION,MARKS) VALUES (3,'Deepu',14,'M',9,'B',458)")
cursor.execute("INSERT INTO STUDENTS(ID,S_NAME,AGE,SEX,CLASS,DIVISION,MARKS) VALUES (4,'Ram',14,'M',9,'A',350)")
cursor.execute("INSERT INTO STUDENTS(ID,S_NAME,AGE,SEX,CLASS,DIVISION,MARKS) VALUES (5,'Athira',14,'F',9,'D',240)")

connection.commit()
connection.close()
