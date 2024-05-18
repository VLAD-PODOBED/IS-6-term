# 9 вариант
# L - VIII
# M - II
# R - IV
# Re - B
# LiMiRi - 1-0-1

import matplotlib.pyplot as plt

message = 'PODOBEDVLADISLAVGEORGIEVICH'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
left_rotor = 'FKQHTLXOCBJSPDZRAMEWNIUYGV'
middle_rotor = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
right_rotor = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
reflector = {
    'A': 'Y',
    'B': 'R',
    'C': 'U',
    'D': 'H',
    'E': 'Q',
    'F': 'S',
    'G': 'L',
    'H': 'D',
    'I': 'P',
    'J': 'X',
    'K': 'N',
    'L': 'G',
    'M': 'O',
    'N': 'K',
    'O': 'M',
    'P': 'I',
    'Q': 'E',
    'R': 'B',
    'S': 'F',
    'T': 'Z',
    'U': 'C',
    'V': 'W',
    'W': 'V',
    'X': 'J',
    'Y': 'A',
    'Z': 'T'
}

print('Сообщение:\t', message)
print('Алфавит:\t', alphabet)
print('Правый ротор:\t', right_rotor)
print('Средний ротор:\t', middle_rotor)
print('Левый ротор:\t', left_rotor)
print('Рефлектор:\t', reflector)

def enigma(message : str, left_rotor : str, middle_rotor : str, right_rotor : str) -> str:
    res = ''
    for character in message:
        letter = right_rotor[alphabet.index(character)]
        letter = middle_rotor[alphabet.index(letter)]
        letter = left_rotor[alphabet.index(letter)]
        letter = reflector[letter]
        letter = alphabet[left_rotor.index(letter)]
        letter = alphabet[middle_rotor.index(letter)]
        letter = alphabet[right_rotor.index(letter)]
        res += letter
        left_rotor = left_rotor[1:] + left_rotor[:1]
        middle_rotor = middle_rotor[0:] + middle_rotor[:0]
        right_rotor = right_rotor[1:] + right_rotor[:1]
    return res

encrypted = enigma(message, left_rotor, middle_rotor, right_rotor)
print('Зашифрованное сообщение:', encrypted)
print('Расшифрованное сообщение:', enigma(encrypted, left_rotor, middle_rotor, right_rotor))

def get_letters_amount(seq):
    letters_dictionary = {}
    for i in seq:
        if i.isalpha():
            if i not in letters_dictionary:
                letters_dictionary[i] = 0
            letters_dictionary[i] += 1
    return dict(sorted(letters_dictionary.items()))

message_probs = get_letters_amount(message)
encrypted_probs = get_letters_amount(encrypted)

fig, a = plt.subplots(2,1, figsize=(12, 10))
a[0].set_title('Исходное сообщение')
a[0].bar(list(message_probs.keys()), message_probs.values(), color='g')
a[1].set_title('Зашифрованное сообщение')
a[1].bar(list(encrypted_probs.keys()), encrypted_probs.values(), color='b')
plt.show()