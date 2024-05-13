import re

def pig_it_helper(word:str):
    return  word if re.match("^\W+$", word) else f"{word[1:]}{word[0]}ay"
    # use word.isalnum

def pig_it(text:str):
    text_arr = text.split(" ")
    return " ".join([pig_it_helper(word) for word in text_arr])

print(pig_it('!')) #igPay atinlay siay oolcay