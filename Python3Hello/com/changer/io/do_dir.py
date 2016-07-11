import os
from datetime import datetime

pwd = os.path.abspath(".")

print("  Size  LastModifiedTime  Name  Flag")
print("------------------------------------------")

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime("%Y-%m-%d %H:%M:%S")
    flag = "/" if os.path.isdir(f) else ""
    print("%10d  %s  %20s  %s" %(fsize, mtime, f, flag))