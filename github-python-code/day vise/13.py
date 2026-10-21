n = int(input("Enter a number: "))

# Positive / Negative / Zero
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Even / Odd
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Divisible by 5
if n % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")