# Find the factorial of a number using while loop.

num=int(input("Enter number for Factorial="))
s =1
while num>=1:
    s=s*num
    num-=1
print(f"Factorial=",s)

# Find the factorial of a number using for loop.

num=int(input("Enter number for Factorial="))
s =1
for a in range(1,num+1):
    s*=a
print(f"Factorial=",s)