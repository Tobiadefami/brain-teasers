
def even_fibonacci_numbers(max_num:int) -> int:
    first, second = 1, 2
    total: int = 0
    for _ in range(max_num):
        if first < max_num:
            if first % 2 == 0:
                total += first
        else:
            break
        first, second = second, first+second
    return total                

    
if __name__ == "__main__":
    num = 4000000
    print(even_fibonacci_numbers(num))