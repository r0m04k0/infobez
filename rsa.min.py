import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = mod_inv(e, phi)
    
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    e, n = pk
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    d, n = pk
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

print(public_key, private_key)

text = "Hello, World!"
encrypted_text = encrypt(public_key, text)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = decrypt(private_key, encrypted_text)
print("Расшифрованный текст:", decrypted_text)
