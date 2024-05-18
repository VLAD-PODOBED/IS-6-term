# • выполнять зашифрование/расшифрование текстовых документов (объемом не менее 500 знаков)
# Русский
# 1. Маршрутная перестановка (маршрут – по спирали; параметры таблицы – по указанию преподавателя)
# 2. Множественная перестановка, ключевые слова – собственные имя и фамилия
# формировать гистограммы частот появления символов для исходного и зашифрованного сообщений;
# • оценивать время выполнения операций зашифрования/расшифрования
import matplotlib.pyplot as plt
from spiral_rout_cipher import *
from multiple_permutation import *

keyword_column = 'подобед'
keyword_row = 'владислав'
with open('m1.txt',  encoding='utf8') as file:
    message = file.read().lower()

message_probs = get_letters_amount(message)
spiral_probs = spiral_route_cipher(message, 4)
print('\n////////////////////////////////////////////////////')
multiple_probs = multiple_permutation(keyword_column, keyword_row, message)

#строим гистограммы по словарям
fig, a = plt.subplots(2,2, figsize=(12, 10))
a[0][0].set_title('Исходное сообщение')
a[0][0].bar(list(message_probs.keys()), message_probs.values(), color='g')
a[0][1].set_title('Спираль')
a[0][1].bar(list(spiral_probs.keys()), spiral_probs.values(), color='b')
a[1][0].set_title('Множественная перестановка')
a[1][0].bar(list(multiple_probs.keys()), multiple_probs.values(), color='r')
plt.show()