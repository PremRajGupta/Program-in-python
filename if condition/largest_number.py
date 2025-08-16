# Find the largest of three numbers.

a = int(input("Enter First Number="))
b = int(input("Enter Second Number="))
c = int(input("Enter Third Number="))

if a>b and a>c:
    print(f"{a} is greatest Number.")
elif b>a and b>c:
    print(f"{b} is greatest Number.")
else:
    print(f"{c} is greatest Number.")
    
    