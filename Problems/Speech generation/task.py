digits = ["zero", "one", "two", "three", "four", "five",
          "six", "seven", "eight", "nine"]
phone_number = list(input())


for i in phone_number:
    print(digits[int(i)])
