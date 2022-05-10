import appapi as app
from fileapi import *
from encode import *
import time
import psutil
import sys

sys.path.append('C:/aydin-os/apps')

battery = psutil.sensors_battery()
app.py_to_app('apps/commandline.py','os.aydin-os.system.commandline')

while True:
    print(time.strftime("%H:%M:%S"))
    print(time.strftime("%d/%m/%Y"))
    print(f"{battery.percent}%")
    print("1: open an app\n2: view the eula\n3: exit")
    do = input("What do you want to do? ")
    if do == "1":
        apps = app.apps()
        for i in range(len(apps[:-1])): # visual studio
            print(f"{i+1}: {apps[i].split('.')[3]}")
        app_num = input("Which app do you want to open (number)? ")
        app.execute_app(apps[int(app_num)-1])
    elif do == '2':
        print(read_file('/system/apps/eula.txt'))
    elif do == '3':
        break

print("shutting down...")
exit(0)