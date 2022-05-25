from datetime import datetime as d
import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
# sql = "insert into dept values(50,'database','seoul')"
# cursor.execute(sql)


while True :
    choice = input('''메뉴를 입력해주세요 
    1. 입고기록 수정  2. 과일목록 수정  3. 원산지 수정  4. 입고기록 보기  5. 프로그램 종료
    >>> ''')

    if choice == '1' :
        menu = input('''1. 추가 
>>> ''')
        if menu == '1' :    
            while True :
                conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
                cursor = conn.cursor()
            #
                sql = "insert into price values(:1,:2)"  #name1, price1
                sqll= "insert into fruit values(:1,:2,:3,:4)"  #name,stock,come,loc_num
                sql2 = "select * from price"
                bill = cursor.execute(sql2)

                print('----- <과일 목록> -----')
                for item in bill :
                    print(item[0], item[1])
                print('-----------------------')
                name1 = input('과일명 >>> ')
                if name1.lower() == 'q' :
                    print('메뉴로 돌아갑니다.')
                    break

                stock1 = int(input('입고량 >>> '))
                come = d.now().date()  #현재 날짜

                sql3 = "select * from loc"
                locate = cursor.execute(sql3)

                print('------ <원산지> ------')
                for item1 in locate :
                    print(item1[0],item1[1])
                print('----------------------')
                loc_num = int(input('원산지번호 >>> ')) 
            #   
                price1=0
                data1 = name1,price1
                data2 = (name1, stock1, come, loc_num)
                
                cursor.execute(sql,data1)
                cursor.execute(sqll,data2)
                print('입고 완료')
                print('-> ', name1, stock1, come, loc_num)
                print('\n')

                cursor.close()
                conn.commit()
                conn.close()


    elif choice == '2' :
        menu = input('''1. 추가  2. 삭제 
>>> ''')
        if menu == '1' :
            while True :
                conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
                cursor = conn.cursor()

                sql = "update price set price1=:1 where name1=:2"
                sql2 = "select * from price"
                bill2 = cursor.execute(sql2)
                print('----- <과일 목록> -----')
                for i in bill2 :
                    print(i[0],i[1])
                print('-----------------------')

                name1 = input('추가할 과일명 >>> ')
                if name1.lower() == 'q' :
                    print('메뉴로 돌아갑니다.')
                    break
                price1 = input('가격 >>> ')
                data = (price1,name1)
                cursor.execute(sql,data)
                print('추가 완료')
                print('\n')

                cursor.close()
                conn.commit()
                conn.close()


        elif menu == '2' :
            conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
            cursor = conn.cursor()

            delete = input('삭제할 과일명 >>> ')
            cursor.execute("delete from fruit where name1 = '" + delete + "'")
            cursor.execute("delete from price where name1 = '" + delete + "'")
            cursor.close()
            conn.commit()
            conn.close()


    elif choice == '3' :
        menu = input('''1. 추가  2. 삭제 
>>> ''')
        if menu == '1' :
            while True :
                conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
                cursor = conn.cursor()

                sql = "insert into loc values(:1,:2)"
                sql2 = "select * from loc"
                locate2 = cursor.execute(sql2)
                print('------ <원산지> ------')
                for j in locate2 :
                    print(j[0], j[1]) 
                print('----------------------')

                loc1 = input('추가할 원산지 >>> ')
                if loc1.lower() == 'q' :
                    print('메뉴로 돌아갑니다.')
                    break
                loc_num1 = int(input('원산지 번호 >>> '))
                data = (loc_num1, loc1)
                cursor.execute(sql, data)
                print('추가 완료')
                print('\n')
                    
                cursor.close()
                conn.commit()
                conn.close()

        elif menu == '2' :
            conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
            cursor = conn.cursor()


            delete = input('삭제할 원산지 >>> ')
            cursor.execute("delete from loc where loc1 = '" + delete + "'")

            cursor.close()
            conn.commit()
            conn.close()



    elif choice == '4' :
        conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
        cursor = conn.cursor()

        sql = "select * from fruit"
        welcome = cursor.execute(sql)

        print('           <입고 현황>            ')
        print('과일명  ', '입고량  ', '입고날짜  ', '원산지no.')
        print('----------------------------------------')
        for w in welcome :
            print(w[0], w[1], w[2].date(), w[3])
        print('\n')

        cursor.close()
        conn.commit()
        conn.close()

    elif choice == '5' :
        print('프로그램을 종료합니다.')
        break