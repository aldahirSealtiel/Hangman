word = input()

ans = ""
for i in word:
    if i.isupper():
        ans += "_" + i.lower()
    else:
        ans += i
print(ans)
