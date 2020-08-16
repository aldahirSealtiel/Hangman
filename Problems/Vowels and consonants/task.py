word = input()
vowels = "aeiou"
for letter in word:
    if not letter.isalpha():
        break
    if letter in vowels:
        print("vowel")
    else:
        print("consonant")