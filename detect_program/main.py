import string

def is_pangram(s:str):
    for i in range(65, 91): # A - Z : 65 - 90
        if chr(i) not in s.upper():
            return False
        
    return True

def is_pangram_flex(s):
    return set(string.ascii_lowercase).issubset(s.lower())