#cryptography
<hr>

#### Description

I found this cipher in an old book. Can you figure out what it says? Connect with `nc jupiter.challenges.picoctf.org 58295`.

#### Solve
1.  `nc jupiter.challenges.picoctf.org 58295`
2. Copy the part `hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xf966878l}`
3. Searching la cifra de cipher on google leads to Vigenere cipher
4. With https://www.dcode.fr/vigenere-cipher, bruteforce the ciphertext with decryption method "Knowing a plaintext word" set to pico
5. picoCTF{b311a50_0r_v1gn3r3_c1ph3ra966878a}