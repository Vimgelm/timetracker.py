import pymysql
import time


def getCurDay():  # данные для сегодня (для графиков)
    con = pymysql.connect(host='localhost',
                      user='root',
                      password='My35al!#',
                      db='timetracker')
    cursor = con.cursor()
    cursor.execute("SELECT prog_name, time, prog_id FROM prog WHERE date = CURDATE()")
    result = cursor.fetchall()
    cursor.close()
    plot_arr = listForPlot(result)
    print(plot_arr)
    return plot_arr

def getTitleForProg(prog_id):  #все заголовки окон для определенной программы
    con = pymysql.connect(host='localhost',
                      user='root',
                      password='My35al!#',
                      db='timetracker')
    cursor = con.cursor()
    cursor.execute("SELECT title, time, date FROM title WHERE prog_id = %s",(prog_id))
    result = cursor.fetchall()
    date = listForTable(result)
    print(date)
    return date

def listForPlot(db_list):   # возращает подготовленные массивы для построения графиков
    plot_arr = [[],[],[]]
    for key in db_list:
        name = filterTitle(key[0])
        time_in_hour = convertTime(key[1])
        name = name+' '+time_in_hour
        plot_arr[0].append(name)
        plot_arr[1].append(key[1])
        plot_arr[2].append(key[2])
    return plot_arr

def listForTable(db_list):  # форматирует в подходящий формат для Dash data table
    table_arr = []
    i=0
    while i<len(db_list):
        table_arr.append({})
        table_arr[i]['title'] = db_list[i][0]
        table_arr[i]['time'] = db_list[i][1]
        table_arr[i]['date'] = db_list[i][2]
        i = i+1
    return table_arr

def convertTime(time_in_sec): #возращает время в формате hh:mm:ss
    time_in_hour = time.strftime("%H:%M:%S", time.gmtime(time_in_sec))
    return time_in_hour

def filterTitle(name): #приводит все название программ к одному формату
    name = name.strip('"')
    name = name.replace('-',' ')
    return name