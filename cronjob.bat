
@echo off

:loop
python c:/Users/ACER/Desktop/awing/awing-autodisconnect.py
python c:/Users/ACER/Desktop/awing/awing-autoconnect.py
timeout /t 600 >nul
goto loop
