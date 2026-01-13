from itertools import permutations

def generate_permutations(s: str, k: int) -> None:
    perms = permutations(s, k)

    for perm in sorted(perms):
        print(''.join(perm))

if __name__ == "__main__":
    s, k = input().split()
    k = int(k)
    generate_permutations(s, k)