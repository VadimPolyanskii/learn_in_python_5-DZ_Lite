# Модуль
import math

# 1. Проверка числа на простоту
number = 61


def prime_numbers(x):
    d = 2
    while x % d != 0:
        d += 1
    return d == x


print('Число', number, 'простое? -', prime_numbers(number))
print('---' * 16)

# 2. Выводим список всех делителей числа.
b = 855


def divisors(a):
    for i in range(a - 1, 1, -1):
        if a % i == 0:
            print(i, end=' ')
    return


divisors(b)


# 3. Выводим самый большой простой делитель числа.


def divisor(a):
    lst = []
    d = 2
    while d * d <= a:
        if a % d == 0:
            lst.append(d)
            a //= d
        else:
            d += 1
    if a > 1:
        lst.append(a)
    return lst


print('Наибольший простой делитель числа', b, '=', max(divisor(b)))