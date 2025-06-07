def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

two_digit_primes = [number for number in range(10, 100) if is_prime(number)]
print(two_digit_primes)