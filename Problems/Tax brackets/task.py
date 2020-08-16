income = int(input())
tax = 0

if 0 <= income < 15528:
    tax = 0
elif 15528 <= income < 42708:
    tax = 15
elif 42708 <= income < 132407:
    tax = 25
else:
    tax = 28

print("The tax for {income} is {percent}%. That is "
      "{calculated_tax:.0f} dollars!".format(income=income,
                                             percent=tax,
                                             calculated_tax=income * tax / 100.0))
