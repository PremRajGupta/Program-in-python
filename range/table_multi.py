# print the multiplication table number using range.

n=int(input("Enter number="))

for a in range(1,11):
    # print(n,"x",a,"=",a*n)
    print(f"{n}x{a}=",a*n)