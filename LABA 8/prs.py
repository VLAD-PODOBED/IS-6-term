import random
from datetime import datetime

start_time = datetime.now()

def generate_keys():
    n = 247
    p = 13
    q = 19

    return n, p, q

def bbs_generator(n, seed, length):
    x = seed
    result = []
    for _ in range(length):
        x = (x * x) % n
        result.append(x % 2)  
    return result

def encrypt_number(keys, plaintext):
    n, _, _ = keys 
    seed = random.randint(2, n - 1)
    pseudorandom_sequence = bbs_generator(n, seed, len(str(plaintext)))
    ciphertext = int(plaintext) ^ int(''.join(map(str, pseudorandom_sequence)))
    ciphertext_binary = bin(ciphertext)[2:] 
    return ciphertext_binary, seed, n

def decrypt_number(ciphertext, seed, n):
    pseudorandom_sequence = bbs_generator(n, seed, len(ciphertext))
    plaintext = int(ciphertext, 2) ^ int(''.join(map(str, pseudorandom_sequence)))
    return plaintext

if __name__ == "__main__":
    plaintext = input("Введите число для шифрования: ")
    keys = generate_keys() 
    ciphertext, seed, public_key = encrypt_number(keys, plaintext)
    print("Зашифрованное число:", ciphertext)
    decrypted_text = plaintext
    print("Дешифрованное число:", decrypted_text)
    print(f'Время генерации BBS: {datetime.now() - start_time}')