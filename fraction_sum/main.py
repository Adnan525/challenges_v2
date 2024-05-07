import math

def fraction(a, b):
    sum = 0
    small_val = min(a,b)
    for i in range(1, small_val+1):
        if a%i == 0 and b%i == 0:
            sum = a/i + b/i
            
    return sum

def fraction_optim(a, b):
    return int(a/math.gcd(a, b) + b/math.gcd(a, b))

print(fraction_optim(2, 4))