import os

os.system("powershell -Command \"(New-Object Net.WebClient).DownloadFile('https://github.com/mcberg1/GrabCAD-Force-Install/blob/main/GrabCAD.zip?raw=true', 'C:\\Users\\%USERNAME%\\Desktop\\GrabCAD.zip')\"")
os.system("powershell -command \"Expand-Archive C:\\Users\\%USERNAME%\\Desktop\\GrabCAD.zip C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\GrabCAD\"")
os.system("del \"C:\\Users\\%USERNAME%\\Desktop\\GrabCAD.zip\"")
os.system("powershell \"$s=(New-Object -COM WScript.Shell).CreateShortcut('%userprofile%\Start Menu\Grab CAD Desktop.lnk');$s.TargetPath='C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\GrabCAD\\GrabCAD\\GrabCADDesktopClient\\GrabCADDesktopClient.exe';$s.Save()\"")
os.system("powershell \"$s=(New-Object -COM WScript.Shell).CreateShortcut('%userprofile%\Desktop\Grab CAD Desktop.lnk');$s.TargetPath='C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\GrabCAD\\GrabCAD\\GrabCADDesktopClient\\GrabCADDesktopClient.exe';$s.Save()\"")




