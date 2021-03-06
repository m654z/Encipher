# Encipher

Encipher makes it easy for you to encode and decode text.

Encipher takes the input and encodes it, and then generates a random key for decoding it. To decode the text, all you need is the encoded version and the key.

It's simple, easy and relatively secure.

Example
-------

**Input:** `encode("Hello, world!")`

**Output:** `['\x82U\\`_"\x1cG_D\\V\x15', '5102476091813']`

The first list item is the text, and the second is your key. To decode it:

**Input:** `decode('\x82U\\`_"\x1cG_D\\V\x15', '5102476091813')`

**Output:** `Hello, world!`

Algorithm
---------

Encipher's algorithm is actually quite simple. I'll try to explain it here.

1. Encipher encrypts the original text using XOR encryption.
2. Encipher generates a string of random numbers as long as the plaintext. `Hello -> 18284`
3. The plaintext is converted into the respective ASCII values. `72 101 108, etc.`
4. The random numbers are added to the ASCII values of the plaintext. `72 + 1 = 73, 101 + 8 = 109, etc.`
5. The ASCII values are converted into characters again. `Imnts`

To decode it, all you need are the random numbers (the key) and the ciphertext. Just do the algorithm backwards.
