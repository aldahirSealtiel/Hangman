# put your python code here
acum = int(input())
square_sum = acum * acum

while acum != 0:
    num = int(input())
    acum += num
    square_sum += num * num

print(square_sum)