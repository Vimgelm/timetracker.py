# init modules
import subprocess
import time
import MainModel

# all global variables
time_sleep = 3
last_title = ""
life_time = 0

def calc_time(current_title):
    global last_title
    global life_time
    if current_title == last_title: #программа продолжает работать
        life_time = life_time + time_sleep
        print('1')
        print(life_time)
    elif current_title != last_title:
        Db = MainModel #сохранить все в базу
        last_title = current_title
        life_time = 0
        print('2')


i = 1
while i == 1:
    rt = subprocess.run(["xdotool", "getactivewindow", "getwindowname"], stdout=subprocess.PIPE)
    current_title = rt.stdout.decode('utf-8')  # title в utf
    calc_time(current_title)
    print(rt.stdout.decode('utf-8'))
    time.sleep(time_sleep)
