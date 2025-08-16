# Check whether a Number is a palindrome or not.

num=int(input("Enter Digit Number="))

num_str= str(num)
if num_str == num_str[::-1]:
    print("Its Palindrome Number")
else:
    print("Its Not Palindrome Number")