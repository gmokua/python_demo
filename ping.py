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
    with open("dext.txt", "w") as file:
        file.write(status)
    print(status)
