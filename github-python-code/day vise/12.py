previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))

units = current - previous

bill = units * 5.50 + 100

print("Units consumed =", units)
print("Total bill =", bill)