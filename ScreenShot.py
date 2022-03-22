import time
import subprocess


def connect_adb():
    print('连接开始')
    subprocess.Popen('adb connect 172.16.250.248:5555', shell=True)
    print('正在连接... \n')
    time.sleep(3)



# connect_adb() 
print('开始截图')

localtime = time.localtime(time.time())
itime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))

print(itime)
subprocess.Popen('adb shell screencap -p /sdcard/' + itime + '.png',shell=True)

time.sleep(2)

subprocess.Popen('adb pull /sdcard/'+ itime +'.png',shell=True)


print('Done')

