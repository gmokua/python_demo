x = input("Type a number: ")
y = input("Type another number: ")

sum = int(x) + int(y)

print("The sum is: ", sum)
#===================================
price = 49.1236457                       
txt = "The Price is {:.2f} ksh"  
print(txt.format(price))         
#===================================

                #Dates
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%B"))