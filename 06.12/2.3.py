a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a % b == 0:
    print(f'{a} делится на {b} нацело')
    print(f'Частное: {a // b}')
else:
    print(f'{a} не делится на {b} нацело')
    print(f'Частное: {a // b}')
    print(f'Остаток: {a % b}')