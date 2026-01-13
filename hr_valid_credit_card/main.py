import re

def validate_credit_card(card_number: str) -> bool:
    pattern = r"^[456](\d{15}|\d{3}-\d{4}-\d{4}-\d{4})$"
    
    if re.match(pattern, card_number):
        card_number = card_number.replace("-", "")
        counter = 1
        for i in range(len(card_number)):
            if counter > 3:
                return False
            try:
                if card_number[i] == card_number[i + 1]:
                    counter += 1
                else:
                    counter = 1
            except IndexError:
                continue
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        card_number = input().strip()
        if validate_credit_card(card_number):
            print("Valid")
        else:
            print("Invalid")