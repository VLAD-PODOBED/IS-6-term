# Генерация ПСП Вариант 3 BBS p, q, e – 256-разрядные числа
# Алгоритм RC4  Вариант 9  n = 6 Ключ: 61, 60, 23, 22, 21, 20, оценка скорости

from rc4 import key_scheduling, rc4_encrypt, rc4_decrypt, stream_generation
from datetime import datetime

start_time = datetime.now()
print('--------------- RC4 ---------------')
print('Введите сообщение:')
message = input()
key = '61 60 23 22 21 20'
print(f'RC4 ключ: {key}')
cipher = rc4_encrypt(message, key)
print(f'Зашифрованное сообщение: {cipher}')
decipher = rc4_decrypt(cipher, key)
print(f'Дешифрованное сообщение: {decipher}\n')
gen = stream_generation(key_scheduling([ord(char) for char in key]))
print(gen)
print(f'Время генерации RC4: {datetime.now() - start_time}')