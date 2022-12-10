  # Функции валидации входных данных (для калькулятора например): valid_float - вещественные числа, valid_int - целые числа.
def valid_float(f):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    i = 'a'
    a = 2
    while a > 1:
        while i not in num:
            if f == '':
                f = input('Введите число: ')
            else:
                for i in f:
                    if i not in num:
                        f = input('Введите число: ')
                        break
        i = 'a'
        a = 0
        for j in f:
            if j == '.':
                a += 1
                if a > 1:
                    f = input('Точка должна быть одна: ')
                    break
                elif f == '.':
                    a = 2
                    f = input('Введите число, а не просто точку: ')
    return float(f)

def valid_int(f):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 'a'
    while i not in num:
        if f == '':
            f = input('Введите целое число: ')
        else:
            for i in f:
                if i not in num:
                    f = input('Введите целое число: ')
                    break
    return int(f)
# Тесты
x = input('Введите первое число: ')
y = input('Введите второе число: ')
x = valid_float(x)
y = valid_int(y)
print(x, type(x), sep=' ')
print(y, type(y), sep=' ')
