def helper_blow_candles(candles_string_arr):
    return ''.join(map(lambda val: str(max(0, int(val) - 1)), candles_string_arr))

def blow_candles(string):
    if all(char == '0' for char in string) or string == "":
        return 0

    if string[0] == '0' and len(string) > 3:
        return 0 + blow_candles(string[1:])

    else:
        candles_string_arr = list(string[:3]) if len(string) > 3 else list(string)
        result = helper_blow_candles(candles_string_arr)
        mod_str = result + string[3:] if len(string) > 3 else result
        return 1 + blow_candles(mod_str)
