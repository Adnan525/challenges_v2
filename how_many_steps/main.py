import math
def how_many_step(a, b):
    count = math.log2(b/a)
    if count < 1:
        return b-a
    elif int(count) - count == 0.0:
        return int(count)
    else:
            if b % 2 == 0 and b//2 <= a: 
                return 1 if b//2 == a else a-b/2
            else:
                return 1 + how_many_step(a, b//2) if b%2 == 0 else 1 + how_many_step(a, b-1)

print(how_many_step(1, 63))