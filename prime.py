# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

# Take input from user
num = int(input("Enter a number: "))

# Check and print result
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")