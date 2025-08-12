import random

time=1
print("You have 3 Times")
rand=random.randint(1,100)
while time<=3:
    a=int(input("Enter Number 1 to 100="))
    if a==rand:
        print("You Win")
        break
    elif a<rand:
        print("Try to Small number") 
    else:
        print("Try to Biggest Number")
    time+=1
        