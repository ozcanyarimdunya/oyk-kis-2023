from datetime import datetime
import time
import os

c = 0
while False:
    now = datetime.now()
    print(now.hour, now.minute, now.second)
    time.sleep(c)
    if now.hour == 12 and now.minute == 34:
        print("yayy")
    os.system("clear")

    print(os.listdir("/"))


files = os.listdir("/Users/ozcan.yarimdunya/Desktop")

for i in files:
    print(i)

