import subprocess
import time
notify = "notify-send 'Hello world!' 'This is an example notification.' --icon=dialog-information"



def send():
    i = 1
    while i == 1:
        subprocess.check_output(notify, shell=True)
        time.sleep(20)