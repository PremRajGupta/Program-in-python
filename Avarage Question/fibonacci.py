# Print the Fibonacci series up to n terms.

num = int(input("Enter Number="))

a,b,c=0,1,0

i=0
while i<=num:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i+=1