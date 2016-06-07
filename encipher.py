import random
import string

def encode(text):
    digits = list(string.digits)
    text = list(text)
    pword = ""
    for i in range(0, len(text)):
        pword += str(random.choice(digits))
        
    key = list(str(pword))
        
    encoded = ""
    keyI = 0
    for c in text:
        encoded += chr(ord(c) + int(key[keyI]))
        keyI += 1

    return [encoded, ''.join(key)]

def decode(text, key):       
    text = list(text)
    pword = ""
    for i in range(0, len(key)):
        pword += str(key[i])

    key = list(str(pword))
        
    decoded = ""
    keyI = 0
    for c in text:
        decoded += chr(ord(c) - int(key[keyI]))
        keyI += 1

    return decoded
