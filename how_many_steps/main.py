import math
def helper(n, const_a):
    if n % 2 == 0 and n//2 <= const_a: 
        if n//2 == const_a:
            return 1
        elif n//2 < const_a:
            return n - const_a
    else:
        if n%2 == 0:
            return 1 + helper(n//2, const_a)
        elif n%2 == 1:
            return 1 + helper(n-1, const_a)


def how_many_step(a, b):
    count = math.log2(b/a)
    if count < 1:
        return b-a
    elif int(count) - count == 0.0:
        return int(count)
    else:
        return helper(b, a)
print(how_many_step(1, 63))