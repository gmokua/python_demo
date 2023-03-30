print("Hello")
name = input("What is your name?\n")
if name == "George":
    print("you are welcome home")
    exit()
if name == "Sandra" or name == "Danny":
    print("Hello " + name +", Youre are welcome for the party")
    exit()
if name == "Glory":
    print("Hello" + name +", Go bring the vistor some snacks") 
else:
    print("Hello Stranger your are not welcome")
exit()