number = int(input())
count = 0
if number < 2:
    print("This number is not prime")
else:
    for i in range(2, number, 1):
        if not number % i:
            count += 1
    if count > 0:
        print("This number is not prime")
    else:
        print("This number is prime")