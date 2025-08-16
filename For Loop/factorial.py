# Find the factorial of a number using for loop.

num=int(input("Enter number for Factorial="))
s =1
for a in range(1,num+1):
    s*=a
print(f"Factorial=",s)