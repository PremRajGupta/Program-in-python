# Write a python script to check whether a given number is a 3 digit or not.?

num = int(input("Enter 3 Digit number="))

num1 = abs(num)

if num1>=100 and num1<=999:
    print("Yes, This is 3 Digit Number")
else:
    print("No, It is not a 3 Digit Number")