# Find the factorial of a number using while loop.

num=int(input("Enter number for Factorial="))
s =1
while num>=1:
    s=s*num
    num-=1
print(f"Factorial=",s)
