import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()

sql="insert into FRUIT values(:1,:2,:3)"
no1 = input('번호(2자리 숫자) >>>')
name1 = input('과일명 >>> ') 
date1=input('위치 >>> ')
data = (int(no1),name1,date1)

cursor.execute(sql,data)
cursor.close()
conn.commit()
conn.close()


