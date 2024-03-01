# 3 digit numbers -> 100, 999
# iterate through the set of 3 digit numbers
# check if the product is a palindrome? if yes, we keep track of the largest palindrome?

def is_palindrome(number:int) -> bool:
    return str(number) == str(number)[::-1]

def find_largest_palindrome():
    largest_palindrome = 0
    
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j 
            
            if is_palindrome(prod) and prod > largest_palindrome:
                largest_palindrome = prod
    return largest_palindrome


if __name__ == "__main__":
    print(find_largest_palindrome())