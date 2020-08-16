# put your python code here
a = int(input())
b = int(input())
count = 0
acum = 0
for i in range(a, b + 1, 1):
    if i % 3 == 0:
        acum += i
        count += 1
print("{ans}".format(ans=acum / count))
