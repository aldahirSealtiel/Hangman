ans = ""
maximum_number_cats = -1

while 1:
    data = input()
    if data == "MEOW":
        break
    number_cats = int(data.split()[1])
    cafe_name = data.split()[0]
    if number_cats > maximum_number_cats:
        maximum_number_cats = number_cats
        ans = cafe_name

print(ans)
