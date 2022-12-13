from math import *

def valid_float(f):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    i = 'a'
    a = 2
    while a > 1:
        while i not in num:
            if f == '':
                f = input('Ошибка! Введите число: ')
            else:
                for i in f:
                    if i not in num:
                        f = input('Ошибка! Введите число: ')
                        break
        i = 'a'
        a = 0
        for j in f:
            if j == '.':
                a += 1
                if a > 1:
                    f = input('Ошибка! Точка должна быть одна: ')
                    break
                elif f == '.':
                    a = 2
                    f = input('Ошибка! Введите число, а не просто точку: ')
    return float(f)

n = []
while n != 'end':
    x = input('Введите первое число: ')
    x = valid_float(x)
    operation = input('Введите один из знаков операции: "+", "-", "*", "/", взятие остатка от деления - "mod", возведение в степень - "pow", целочисленное деление - "div": ')
    operations = ['+', '-', '*', '/', 'mod', 'pow', 'div']
    while operation not in operations:
        operation = input('Ошибка! Введите один из знаков операции: "+", "-", "*", "/", взятие остатка от деления - "mod", возведение в степень - "pow", целочисленное деление - "div": ')
    y = input('Введите второе число: ')
    y = valid_float(y)
    if operation == '+':
        print(x, '+', y, '=', x + y)
    elif operation == '-':
        print(x, '-', y, '=', x - y)
    elif operation == '*':
        print(x, '*', y, '=', x * y)
    elif operation == '/':
        if y != 0:
            print(x, '/', y, '=', x / y)
        else:
            print('Деление на ноль противоречит Конституции Галактики, Вы будете арестованы!!!')
    elif operation == 'mod':
        if y != 0:
            print(x, 'mod', y, '=', x % y)
        else:
            print('Деление на ноль противоречит Конституции Галактики, Вы будете арестованы!!!')
    elif operation == 'pow':
        print(x, 'pow', y, '=', pow(x, y))
    elif operation == 'div':
        if y != 0:
            print(x, 'div', y, '=', x // y)
        else:
            print('Деление на ноль противоречит Конституции Галактики, Вы будете арестованы!!!')
    else:
        print('Штааа?!')
    n = input('Для завершения введите "end", для продолжения просто нажмите Enter: ')