# Write a program to reverse a string.

string=input("Enter String=")

for e in string[::-1]:
    print(e, end="")

# second method
rev = string[::-1]
print(rev)