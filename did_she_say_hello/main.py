# You received a whatsup message from an unknown number. 
# Could it be from that girl with a foreign accent you met yesterday evening?
# Write a simple function to check if the string contains the word hallo in different languages.

# These are the languages of the possible people you met the night before:
# hello - english
# ciao - italian
# salut - french
# hallo - german
# hola - spanish
# ahoj - czech republic
# czesc - polish
# Notes

# you can assume the input is a string.
# to keep this a beginner exercise you don't need to check if the greeting is a subset of word 
# (Hallowen can pass the test)
# function should be case insensitive to pass the tests
# ==============================================================================================

def validate_hello(greetings) -> bool:
    """
    Check if the input string contains a greeting in various languages.
    
    Args:
        greetings (str): The input string to check for greetings.
    
    Returns:
        bool: True if any greeting is found, False otherwise.
    """
    all_hellos = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]

    return any(hello in greetings.lower() for hello in all_hellos)