number_minor = 1000000.0
while 1:
    number = input()
    if number == ".":
        break
    else:
        if float(number) < number_minor:
            number_minor = float(number)
print(number_minor)
