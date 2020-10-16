# Пару можно создать на основе строки. Для хранения двух значений применим разделитель. Им может выступить любой символ, однако во избежание совпадений с исходными данными лучше взять редко используемое значение.

# Для этого подойдёт так называемая управляющая или escape-последовательность, которая начинается с обратной косой черты. Мы будем использовать специальный символ \0, обозначающий нулевой символ (NUL).

# Функции car и cdr должны получить содержимое строки до и после разделителя соответственно.

# Управляющая последовательность воспринимается интерпретатором как одиночный символ, т.е. имеет длину, равную 1.

# Обязательным условием является отсутствие данного символа в строках, которые объединяются в пару.

# pairs.py
# Реализуйте и экспортируйте следующие функции в соответствии с алгоритмом выше:

# cons
# car
# cdr
# Пример
# >>> pair = cons('computer', 'science')
# 'computer\0science'
# >>>
# >>> car(pair)
# 'computer'
# >>> cdr(pair)
# 'science'
# Подсказки
# Для подсчёта длины строки используйте встроенную функцию len().


SEPARATOR = "\0"

def uncons(pair):
    for pos, char in enumerate(pair):
        if char == SEPARATOR:
            return pair[:pos], pair[pos + 1:]
    return pair, ""

def cons(a, b):
    return "{}{}{}".format(a, SEPARATOR, b)

def car(pair):
    return uncons(pair)[0]

def cdr(pair):
    return uncons(pair)[1]

# TAB = "\0"

# def cons(a, b):
#     return '{}{}{}'.format(a, TAB, b)

# def car(pair):
#     return pair.split(TAB)[0]

# def cdr(pair):
#     return pair.split(TAB)[-1]

#_________________

# def cons(x, y):
#     return f"{x}\0{y}"

# def car(pair):
#     return pair.split("\0")[0]

# def cdr(pair):
#     return pair.split("\0")[1]