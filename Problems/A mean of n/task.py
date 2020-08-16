size = int(input())
acum = 0
for _ in range(size):
    num = int(input())
    acum += num
print("{ans}".format(ans=(acum / size)))
