from itertools import cycle
import random
import string

# Simple XOR encryption
def xor(p, k):
    o = ""
    for i, c in enumerate(p):
        o += chr(ord(c) ^ ord(k[i % len(k)]))

    return o

def encode(text):

    digits = list(string.digits)
    text = list(text)
    pword = ""
    
    # Get a random sequence of integers from 0-9
    for i in range(0, len(text)):
        pword += str(random.choice(digits))
        
    key = list(str(pword))
    text = xor(text, key)
    
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

    # Subtract the key from the ASCII values of the ciphertext
    for c in text:
        decoded += chr(ord(c) - int(key[keyI]))
        keyI += 1

    decoded = xor(decoded, key)

    return decoded
