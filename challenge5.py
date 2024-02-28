# OPTIMIZATION:
# utilize the concept of LCM - which is the smallest number that can divide any two numbers
# LCM = a*b/gcd(a, b)
# gcd - greatest common devisor
# iterate through the number range, while omiting 1, and assign the smallest number to the lcm of the smallest number a divisible number


def gcd(a: int,b: int) ->int:
    while b:
        a, b = b, a%b
    return a     


def lcm(a: int, b: int) -> int:
    return (a*b)//gcd(a, b)


def smallest_number_divisible_by(n:int=10) -> int:
    smallest_num = 1
    for i in range(2, n+1):
        smallest_num = lcm(smallest_num, i)
    return smallest_num    



if __name__ == "__main__":
    print(smallest_number_divisible_by(20))
