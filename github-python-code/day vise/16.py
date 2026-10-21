n = int(input("Enter a number: "))

# Check prime
if n < 2:
    print("Not Prime")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")


# Print all prime numbers from 2 to N
print("Prime numbers from 2 to", n)

for num in range(2, n + 1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")