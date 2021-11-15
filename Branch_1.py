from devisor_master import prime_numbers, divisors, divisor, number, b


print('Число', number, 'простое? -', prime_numbers(number))
print('---' * 16)
print(divisors(855))
print('---' * 16)
print('Наибольший простой делитель числа', b, '=', max(divisor(b)))