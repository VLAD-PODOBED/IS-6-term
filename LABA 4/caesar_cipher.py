alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

def remove(keyword : str):
    keyword_list = []
    for character in keyword:
        # удаляем повторяющиеся символы в ключевом слове
        if character not in keyword_list:
            keyword_list.append(character)
        # удаляем символы ключевого слова из алфавита
        if character in alphabet:
            alphabet.remove(character)
    return keyword_list, alphabet

def insert(keyword):
    keyword_alphabet = remove(keyword)
    return keyword_alphabet[0]+keyword_alphabet[1]

def caesar_encrypt(keyword: str, text: str):
    res = ''
    alphabet_list = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    keyword = remove(keyword.lower())[0]
    print('Нормализованное ключевое слово: ',  ''.join(keyword))
    new_alphabet = insert(keyword)
    print('Исходный алфавит:', alphabet_list)
    print('Алфавит с ключем:', new_alphabet)
    for character in text:
            if character in alphabet_list:
                res += new_alphabet[alphabet_list.index(character)]
            else:
                res += character
    return res

def caesar_decrypt(keyword: str, text: str):
    res = ''
    alphabet_list = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    new_alphabet = insert(keyword)
    for character in text:
            if character in new_alphabet:
                res += alphabet_list[new_alphabet.index(character)]
            else:
                res += character
    return res