import os
shutdown = input("Do you wish to shutdown your computer ? (yes / no): ") 
if shutdown == 'no':
    exit()
if shutdown == 'yes':
    os.system("shutdown /s /t 1")
else:
    os.system("shutdown /f /t 1")