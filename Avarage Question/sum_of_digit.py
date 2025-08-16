# Write a program to calculate the sum of digits of a number.
num = int(input("Enter Number="))
total = 0
while num>0:
    digit = num%10
    total+=digit
    num//=10

print(f"Sum of Digit={total}")