# getting prime numbers within a given range
# check to make sure the max prime number does not exceed the predefined limit
from typing import List

def is_prime_number(n:int, primes:List[int]) -> bool:
    if n <= 1:
        return False
    
    sqrt_of_n = int(n**0.5)
    
    for prime in primes:
        if prime > sqrt_of_n:
            return True
        elif prime <= sqrt_of_n and n%prime == 0:
            return False
    return True
            
    
def get_primes(limit: int) ->int:

    primes = []
    value = 2
    while len(primes) < limit:
        if is_prime_number(value, primes):
            primes.append(value)
        value += 1

    return primes[limit-1]

if __name__ == "__main__":
    print(get_primes(100000))