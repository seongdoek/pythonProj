import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()

cursor.execute('''create table price(
name1 varchar2(20) constraint name_p primary key,
price1 number(5) constraint price_c check (price1 between 0 and 50000)
)''')
cursor.execute("insert into price(name1, price1) values('사과',3000)")
cursor.execute("insert into price(name1, price1) values('리치',2500)")

cursor.execute("insert into price(name1, price1) values('애플수박',5000)")
cursor.execute("insert into price(name1, price1) values('체리자두',8000)")
cursor.execute("insert into price(name1, price1) values('샤인머스켓',30000)")
cursor.close()
conn.commit()
conn.close()



conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()

cursor.execute('''create table loc (
loc_num number(3) constraint loc_p primary key,
loc1 varchar2(50)
)''')
cursor.execute("insert into loc(loc_num, loc1) values(10, '한국')")
cursor.execute("insert into loc(loc_num, loc1) values(20, '일본')")
cursor.execute("insert into loc(loc_num, loc1) values(30, '중국')")
cursor.execute("insert into loc(loc_num, loc1) values(40, '브라질')")
cursor.execute("insert into loc(loc_num, loc1) values(50, '멕시코')")
cursor.execute("insert into loc(loc_num, loc1) values(60, '인도네시아')")
cursor.close()
conn.commit()
conn.close()


conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()

cursor.execute('''create table fruit(
name1 varchar2(20) constraint name_f references price(name1),
stock1 number(3), 
come date,
loc_num number(3) constraint loc_f references loc(loc_num)
)''')
#cursor.execute("insert into ")
cursor.close()
conn.commit()
conn.close()