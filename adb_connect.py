import time
import subprocess


def connect_adb():
    print('连接开始')
    subprocess.Popen('adb connect 172.16.250.248:5555', shell=True)
    print('正在连接... \n')
    time.sleep(3)
connect_adb()
print('Done')

