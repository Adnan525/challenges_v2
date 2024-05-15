# from itertools import permutations

# def next_higher(n):
#     test = [byte for byte in bin(n)[2:].zfill(32)]
#     first_one_index = test.index("1")
#     target = test[first_one_index:]
#     target_reverse = target[::-1]
#     first_zero_index = target_reverse.index("0")
#     target_reverse[first_zero_index] = "1"
#     target_reverse[first_zero_index-1] = "0"
#     print(target_reverse)
#     return int("".join(target_reverse[::-1]), 2)

# print(next_higher(201326592))
#     # div, remainder = (test.index("1")-1)//8, (test.index("1")-1)%8
#     # print(div, remainder)
#     # perm = set(list(permutations(test, r = len(test))))
#     # val = sorted([int("".join(binary_string), 2) for binary_string in perm])
#     # print(val)
#     # return val[val.index(n)+1]

# # def next_higher_dumb(n):
# #     target = n
# #     n_binary = bin(n)[2:]
# #     number_of_1 = n_binary.count("1")
# #     while True:
# #         target += 1
# #         if bin(target)[2:].count("1") == number_of_1:
# #             return target