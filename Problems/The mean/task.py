acum = 0
count_number = 0
while 1:
    number = input()
    if number == ".":
        break
    count_number += 1
    acum += int(number)

print(acum / count_number)
