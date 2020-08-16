ans = []
while 1:
    name = input()
    if name == ".":
        break
    ans.append(name)

print("{}\n{}".format(ans, len(ans)))
