def square_digits(num):
    result = [pow(int(c), 2) for c in str(num)]
    return int("".join([str(i) for i in result]))
print(square_digits(3212))