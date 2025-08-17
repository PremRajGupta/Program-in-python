# Print the multiplication table of a number using range().

num = int(input("Enter Number="))
for i in range(1,11,1):
    print(f"{num}x{i}={num*i}")
