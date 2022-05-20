import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()

cursor.execute("select * from emp ")

for item in cursor:
    print( item[2])
    break

conn.close()

