import subprocess
hostfile=open("hosts.txt", "r")
lines=hostfile.readlines()
for line in lines:
    response=subprocess.Popen(["ping", "-c", "1", line.strip()],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
    stdout, stderr = response.communicate()
    #print(stdout)
    #print(stderr)

    if (response.returncode == 0):
        status = line.rstrip() + " is Reachable"
    else:
        status = line.rstrip() + " is Not reachable"
    f = open("text.txt", "w")
    f.write(status)
    f.close()
    f = open("text.txt", "r")
    f.read(status)
    f.close()

    #print(status)