import random

PASS_LEN = 10

# Добавление групп сомволов
NUM = 'YES'
SPECIAL = 'NO'
UPPERCASE = 'YES'
LOWERCASE = 'YES'
SOLT = ''

list1 = []

# Генерация спецсимволов
if SPECIAL == 'YES':
    ascii_values = [chr(i) for i in range(33, 48)]
    list1 += ascii_values
else:
    pass
# Генерация цифр
if NUM == 'YES':
    ascii_values = [chr(i) for i in range(48, 58)]
    list1 += ascii_values
else:
    pass
# Генерация большого регистра
if UPPERCASE == 'YES':
    ascii_values = [chr(i) for i in range(65, 91)]
    list1 += ascii_values
else:
    pass
# Генерация маленького регистра
if LOWERCASE == 'YES':
    ascii_values = [chr(i) for i in range(97, 123)]
    list1 += ascii_values
else:
    pass


def main(passlist):
    res = ''
    for _ in range(PASS_LEN):
        passw = random.choice(list1)
        res += passw
    print(f'Результат: {res + SOLT}')


main(list1)
