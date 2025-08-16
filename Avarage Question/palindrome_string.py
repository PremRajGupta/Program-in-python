# Check whether a string is a palindrome or not.

string= input("Enter String=")

if string == string[::-1]:
    print("This is Palindrome")
else:
    print("This is Not Palindrome")