def maximise_it(l: list[list[int]], m: int) -> int:
    possible_remainders = {x**2 % m for x in l[0]}
    
    for i in range(1, len(l)):
        new_remainders = set()
        for p_r in possible_remainders:
            new_remainders.update(
                [(p_r + x**2) % m for x in l[i]]
            )
        possible_remainders = new_remainders
    
    return max(possible_remainders)

if __name__ == "__main__":
    k, m = map(int, input().split())
    l = []
    for _ in range(k):
        nums = list(map(int, input().split()))
        l.append(nums[1:])
    
    print(maximise_it(l, m))