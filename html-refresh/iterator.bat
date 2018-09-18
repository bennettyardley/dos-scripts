:loop
FOR /L %%A IN (1,1,5) DO (
  ECHO %%A
  START "" run.bat
)
TIMEOUT /T 3000 /NOBREAK
TASKKILL /F /IM python.exe
goto loop