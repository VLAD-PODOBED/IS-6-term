from number_theory import *
from math import *
m = 399
n = 433

print('НОД двух чисел')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число:' ))
print(get_gcd2(a,b))

print('\nНОД трех чисел')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число:' ))
c = int(input('Введите третье число:' ))
print(get_gcd3(a,b,c))

print('\nПоиск простых чисел')
a = int(input('Введите нижнюю границу: '))
b = int(input('Введите верхнюю границу:' ))
print(get_prime(a,b))

print('\nПоиск простых чисел в интервале [2, n]')
print(get_prime(2,n))
print('Количество простых чисел в указанном интервале:', len(get_prime(2,n)))
print('n/ln(n)', n / log(n))

print('\nПоиск простых чисел в интервале [m, n]')
print(get_prime(m,n))
print('Количество простых чисел в указанном интервале:', len(get_prime(m,n)))

print('\nЧисла в виде произведения простых множителей')
print('Простые множители n: ', get_factors(n))
print('Простые множители m: ', get_factors(m))

conc = int(str(m) + str (n))
print('\nЯвляется ли число, состоящее из конкатенации цифр m ǀǀ n простым', is_prime(conc))

print('\nНОД (m, n)', get_gcd2(m, n))