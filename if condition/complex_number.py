# Write a python script to accept one complex number from the user and display 
# the greater number between real part and imaginary part.

num = input("Enter Complex number e.g(3+4j)=")

num1 = complex(num)

real = num1.real
imag = num1.imag

if real>imag:
    print("Grater part is a Real Part",real)
elif imag>real:
    print("Greater part is Imaginary Part",imag)
else:
    print("Both real and imaginary parts are equal=",real)