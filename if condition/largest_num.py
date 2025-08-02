# Write a program to input three numbers and print the largest.

a = int(input("Enter First Numebr="))
b = int(input("Enter Second Numebr="))
c = int(input("Enter Third Numebr="))

if a>b and a>c:
    print(a,"is grater Number")
elif b>c and b>a:
    print(b,"is Greater Number")
else:
    print(c,"is greater Number")