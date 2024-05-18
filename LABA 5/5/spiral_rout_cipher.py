import numpy as np
from datetime import datetime

def form_matrix(message : str, route_step : int) -> np.ndarray:
    message_len = len(message)
    if message_len % route_step != 0:
        message += ' ' * (route_step - message_len % route_step)
    matrix = np.array(list(message), dtype=np.str_)
    matrix = matrix.reshape(route_step, -1)
    return matrix

def encrypt(message : str, route_step : int) -> str:
    message = message.replace('ё', 'е').replace('Ё', 'Е') # замена ё на е
    matrix = form_matrix(message, route_step)
    print('Таблица:')
    for row in matrix:
        print(row)
    res = ''
    i, j = matrix.shape
    for r in range(0, (min(i, j) + 1) // 2):
        for c in range(r, j - r):
            res += matrix[r, c]
        for c in range(r + 1, i - r):
            res += matrix[c, j - r - 1]
        for c in range(j - r - 2, r - 1, -1):
            res += matrix[i - r - 1, c]
        for c in range(i - r - 2, r, -1):
            res += matrix[c, r]
    return res

def decrypt(message: str, route_step : int) -> str:
    message = message.replace('ё', 'е').replace('Ё', 'Е') # замена ё на е
    message_len = len(message)
    if message_len % route_step != 0:
        message += ' ' * (route_step - message_len % route_step)
    matrix = np.empty((route_step, message_len // route_step), dtype=np.str_)
    i, j = matrix.shape
    r_count = 0
    r_start = 0
    r_end = i
    c_count = 0
    c_start = 0
    c_end = j
    for letter in message:
        matrix[r_count, c_count] = letter
        if c_count < c_end - 1 and r_count == r_start:
            c_count += 1
        elif r_count < r_end - 1 and c_count == c_end - 1:
            r_count += 1
        elif c_count > c_start and r_count == r_end - 1:
            c_count -= 1
        elif r_count > r_start and c_count == c_start:
            r_count -= 1
            if r_count == r_start + 1:
                r_start += 1
                r_end -= 1
                c_start += 1
                c_end -= 1
    print('\nТаблица:')
    for row in matrix:
        print(row)
    res = ''.join(matrix.ravel())
    return res

#словарь {символ:количество потворений этого символа} отсортированный по ключу
def get_letters_amount(seq):
    letters_dictionary = {}
    for i in seq:
        if i.isalpha():
            if i not in letters_dictionary:
                letters_dictionary[i] = 0
            letters_dictionary[i] += 1
    return dict(sorted(letters_dictionary.items()))

def spiral_route_cipher(message: str, route_step : int):
    start_time = datetime.now()
    encrypted = encrypt(message, route_step)
    encrypt_time = datetime.now() - start_time
    print('\nЗашифрованное сообщение:', encrypted)
    start_time = datetime.now()
    decrypted = decrypt(encrypted, route_step)
    decrypt_time = datetime.now() - start_time
    print('\nРасшифрованное сообщение:', decrypted)
    print('\nВремя зашифрования:', encrypt_time)
    print('Время расшифрования:', decrypt_time)
    return get_letters_amount(encrypted)