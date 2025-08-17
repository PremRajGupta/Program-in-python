# Print all prime numbers between 1 and 100 using range().

for num in range(1,101,1):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print(num,end=" ")