# Encipher

Encipher makes it easy for you to encode and decode text.

Encipher takes the input and encodes it, and then generates a random key for decoding it. To decode the text, all you need is the encoded version and the key.

It's simple, easy and relativly secure.

Example
-------

**Input:** `encode("Hello, world!")`

**Output:** `["Pjopo1'\x80oynm%", '8534057907294']`

The first list item is the text, and the second is your key. To decode it:

**Input:** `decode("Pjopo1'\x80oynm%", "8534057907294")`

**Output:** `Hello, world!`

