def largest_prime_factor(number: int) -> int:
    
    # using the trial division method because my original implementation 
    # is suboptimal for very large numbers
    
    # choose the smallest factor to divide the number by
    smallest_factor:int = 2
    
    while number > 1:
        if number % smallest_factor == 0:
            # update the number based on the
            number //= smallest_factor
            while number % smallest_factor == 0:
                number //= smallest_factor
        smallest_factor += 1
        
    return smallest_factor -1






if __name__ == "__main__":
    number = 600851475143
    # number = 13195
    print(largest_prime_factor(number))
