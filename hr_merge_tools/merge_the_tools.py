def merge_the_tools(k: str, n: int) -> None:
    substrings = [k[i:i+n]for i in range(0, len(k), n)]
    for substring in substrings:
        print(''.join(dict.fromkeys(substring).keys()))