def sum_square_difference(n):
    sum_squares = 0
    sum = 0
    for i in range(1, n+1):
        sum_squares += i**2
        sum += i
    difference = sum**2 - sum_squares
    return difference
    

if __name__ == "__main__":
    print(sum_square_difference(100))
