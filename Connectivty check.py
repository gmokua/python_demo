import os
hostname = "google.com"
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print (hostname, 'is up!')
  exit()
else:
  print (hostname, 'is down!')
  exit()