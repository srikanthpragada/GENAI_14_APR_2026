

def isprime(n):
    """Returns True if n is a prime number, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_all_factors_directly(n):
    """Prints all factors of n directly."""
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

