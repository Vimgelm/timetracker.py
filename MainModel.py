import pymysql

con = pymysql.connect(host='localhost',
                      user='root',
                      password='My35al!#',
                      db='timetracker')

class DB:
        def insertNewProg(title, prog_name): #добавляет новый сайт в базу
            cursor = con.cursor()
            cursor.execute("INSERT INTO prog (name, time, date) VALUES(%s, %s, CURDATE())", ( prog_name))
            con.commit()
            cursor.close()
            print('insert')

        def updateCurrentTime(title, life_time):  # обновить время если в данные сутки программа запускалась
            cursor = con.cursor()
            cursor.execute("UPDATE prog SET time = time + %s WHERE name = %s AND date = CURDATE()", (life_time, title))
            con.commit()
            cursor.close()
            print('updatetime')
            # обработка ошибок:



        def checkProgDb(prog_name, title, life_time):          # проверяет, потом записывает или обновляет данные в 2 бд prog и title
            cursor = con.cursor()
            cursor.execute("SELECT prog_id FROM prog WHERE prog_name = %s AND date = CURDATE()", (prog_name))
            prog_id = cursor.fetchone()
            cursor.execute("SELECT title_id FROM title WHERE title = %s AND date = CURDATE()", (title))
            title_id = cursor.fetchone()
            print(str(prog_id) + ' ' + str(title_id))
            if prog_id == None and title_id == None:  # проверяет наличие записи 'сегодня' 'имя'
                print('insert new prog')
                cursor.execute("INSERT INTO prog (prog_name, time, date) VALUES(%s, %s, CURDATE())", (prog_name, life_time))
                con.commit()
                cursor.execute("INSERT INTO title (prog_id, title, time, date) VALUES(LAST_INSERT_ID(), %s, %s, CURDATE())", (title, life_time))
                con.commit()
                cursor.close()
            elif prog_id != None and title_id == None:
                print('insert title')
                cursor.execute("INSERT INTO title (prog_id, title, time, date) VALUES(%s, %s, %s, CURDATE())", (prog_id, title, life_time))
                con.commit()
                cursor.close
            elif prog_id != None and title_id != None:
                print('update')
                cursor.execute("UPDATE prog SET time = time + %s WHERE prog_id = %s", (life_time, prog_id))
                con.commit()
                cursor.execute("UPDATE title SET time = time + %s WHERE prog_id = %s AND title = %s", (life_time, prog_id, title))
                con.commit()
                cursor.close()



