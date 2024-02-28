def largest_prime_factor(number: int) -> int:

    # using the trial division method because my original implementation
    # was suboptimal for very large numbers

    # choose the smallest factor to divide the number by
    factor: int = 2

    while number > 1:
        if number % factor == 0:
            # divide the factor out of the number
            number //= factor
            # check if new number is divisible by factor.
            while number % factor == 0:
                # if so, divide the factor out of the new number
                number //= factor
        # update factor
        factor += 1

        # check if the square of the factor is greater than the number
        if factor * factor > number:
            if number > 1:
                return number
            else:
                break

    return factor


if __name__ == "__main__":
    number = 600851475143
    # number = 13195
    print(largest_prime_factor(number))
