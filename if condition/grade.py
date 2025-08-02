''' Write a program that takes marks and prints the grade:
90+ : A
80-89 : B
70-79 : C
60-69 : D
Below 60 : F '''

num = int(input("Enter Marks Number="))

if num>=90:
    print("Grade A")
elif num>=80:
    print("Grade B")
elif num>=70:
    print("Grade C")
elif num>=60:
    print("Grade D")
else:
    print("Grade E")