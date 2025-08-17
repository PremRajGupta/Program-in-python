# Print numbers from 1 to 100 that are divisible by 5 using range().

for i in range(1,101,1):
    if i%5==0:
        print(f"Divisible by 5={i}")