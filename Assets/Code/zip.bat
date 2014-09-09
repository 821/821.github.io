FOR /D %%I IN (*) DO CD %%I&"C:\Program Files\WinRAR\winrar" u -afzip "%%I" *.* -m5&MOVE /Y "%%I".zip ..\&CD ..
PAUSE
