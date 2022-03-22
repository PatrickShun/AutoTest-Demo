import subprocess
import time


def MYTIME():
    mytime = time.localtime(time.time())
    #print("本地时间：",mytime)
    timeNameList = [] 
    for i in mytime:
        timeNameList.append(i)
    MyYear = timeNameList[0]
    Mymon = timeNameList[1]
    MyD = timeNameList[2]
    MyH = timeNameList[3]
    MyM = timeNameList[4]
    MyS = timeNameList[5]
    MyfileName = "adbLog" + str(MyYear) + "-" + str(Mymon) + "-" + str(MyD) + "-" + str(MyH) + str(MyM) + str(MyS) + '.log'
    # print('File Name is OK')
    return MyfileName

def connect_adb():
    print('连接开始')
    subprocess.Popen('adb connect 172.16.250.248:5555', shell=True)
    print('正在连接... \n')
    time.sleep(3)


if __name__ == "__main__":
    connect_adb()
    FileName = MYTIME()
    print('\n 开始抓取adbLog')
    print("FileName：" + FileName)
    #subprocess.Popen('adb logcat -c', shell=True)
    #subprocess.Popen('adb logcat -G 20M', shell=True)

    subprocess.Popen('adb logcat > ' + FileName , shell=True)

    time.sleep(3)
    exitLog = input("\n输入任意字符 或 回车三次停止Log:")

    for i in range(2):
        if exitLog:
            subprocess.Popen('adb kill-server')
        else:
            exitLog = input("输入按1次:")

    subprocess.Popen('adb kill-server')

    print("已停止")









