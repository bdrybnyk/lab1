import re

def length(pswd):
    return len(pswd) >= 8

def digit(pswd):
    return any(char.isdigit() for char in pswd)

def upper(pswd):
    return any(char.isupper() for char in pswd)

def special(pswd):
    special_chars = r"[!@#$%^&*(),.?\":{}|<>]"
    return bool(re.search(special_chars, pswd))

def valid(pswd):
    if not pswd:
        raise ValueError("pswd cannot be empty!")
    
    x = 0
    if length(pswd): x += 1
    if digit(pswd): x += 1
    if upper(pswd): x += 1
    if special(pswd): x += 1
    
    return x