def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def get_prime_numbers(limit):
    primes = []
    value = 2
    while True:
        if is_prime(value):
            primes.append(value)
        elif len(primes) > limit:
            break
        value += 1
    return primes[limit-1]
    
if __name__ == "__main__":
    print(get_prime_numbers(10001))
