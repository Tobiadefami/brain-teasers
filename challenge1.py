

def sum_multiples(number: int) -> int:
    total: int = 0  
    for num in range(number):
        if num%3 == 0:
            total += num
        elif num%5 == 0:
            total += num
    
    return total

if __name__ == "__main__":
    nums = 1000
    print(sum_multiples(nums))