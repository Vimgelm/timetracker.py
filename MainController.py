# init modules
import subprocess
import time
from MainModel import DB
#import app

# all global variables
time_sleep = 3
last_title = "init"
last_prog_name = "init"
life_time = 1


subprocess.Popen('python3 app.py', executable='/bin/bash', shell=True) #запуск flask сервера с визуализацией

def saveCurResult():    #сохранит текущий результат не дожидаясь смены окна
    MainDb = DB
    DB.checkProgDb(last_prog_name, last_title, life_time)

def getProgName():  # вернет имя текущего активного окна
    rt = subprocess.check_output("xprop -id $(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}') | awk '/WM_CLASS\(STRING\)/{print $NF}'", shell=True)
    prog_name = rt.decode('utf-8')
    return prog_name

def getProgTitle(): # вернет заголовок активного окна
    rt = subprocess.run(["xdotool", "getactivewindow", "getwindowname"], stdout=subprocess.PIPE)
    current_title = rt.stdout.decode('utf-8')  # title в utf
    return current_title

def calc_time(current_title):   # подсчитывает время работы активного окна либо сбрасывает счетчик если окно изменилось
    global last_title
    global life_time
    global last_prog_name
    if current_title == last_title:         # программа продолжает работать
        life_time = life_time + time_sleep
        last_prog_name = getProgName()
        print('continue'+' '+last_prog_name+' '+current_title+' '+str(life_time))
    elif last_title == 'init':                  # инициализация prog_name
        last_title = current_title
        print('init' + ' ' + current_title)
    elif current_title != last_title:       # открыто новое окно
        mainDB = DB
        print('start'+' '+last_prog_name+''+last_title +' '+str(life_time))
        mainDB.checkProgDb(last_prog_name, last_title, life_time)
        last_title = current_title
        last_prog_name = "fail"
        life_time = 1

i = 1
while i == 1:
    current_title = getProgTitle()
    calc_time(current_title)
    time.sleep(time_sleep)