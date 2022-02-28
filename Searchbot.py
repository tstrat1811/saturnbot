import time
from datetime import datetime

now=datetime.now()
current_time=now.strftime("%H:%M:%S")
ctime=now.strftime("%H")
date=now.date()
print(ctime)