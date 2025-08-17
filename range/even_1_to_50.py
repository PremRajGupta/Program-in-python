# Print all even numbers between 1 and 50 using range().

for even in range(2,52,2):
    print(even,end=" ")

# Second Method
print("second Method")
for even in range(1,50,1):
    if even%2==0:
        print(even,end=" ")