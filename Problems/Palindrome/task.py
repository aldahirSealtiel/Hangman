word = input()
i = 0
j = len(word) - 1
is_palindrome = True
while i < j:
    if word[i] != word[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not palindrome")
