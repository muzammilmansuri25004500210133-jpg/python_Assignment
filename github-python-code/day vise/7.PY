n = int(input("Enter a 3-digit number: "))

hundreds = n // 100
tens = (n // 10) % 10
units = n % 10

sum_digits = hundreds + tens + units
product = hundreds * tens * units

print("Hundreds =", hundreds)
print("Tens =", tens)
print("Units =", units)
print("Sum =", sum_digits)
print("Product =", product)