import random
import string

def encode(text):
    digits = list(string.digits)
    text = list(text)
    pword = ""
    
    # Get a random sequence of integers from 0-9
    for i in range(0, len(text)):
        pword += str(random.choice(digits))
        
    key = list(str(pword))
    
    encoded = ""
    keyI = 0

    # Add the random sequence to the ASCII values of the string
    for c in text:
        encoded += chr(ord(c) + int(key[keyI]))
        keyI += 1

    return [encoded, ''.join(key)]

def decode(text, key):
    text = list(text)
    pword = str(key)

    key = list(str(pword))
        
    decoded = ""
    keyI = 0
    for c in text:
        decoded += chr(ord(c) - int(key[keyI]))
        keyI += 1

    return decoded
