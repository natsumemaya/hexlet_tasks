#Реализуйте функцию compare_version, которая сравнивает переданные версии version1 и version2. Если version1 > version2, то функция должна вернуть 1, если version1 < version2, то -1, если же version1 = version2 — 0.

#Версия — это строка, в которой два числа (мажорная и минорные версии) разделены точкой, например: 12.11. Важно понимать, что версия — это не число с плавающей точкой, а несколько чисел не связанных между собой. Проверка на больше/меньше производится сравнением каждого числа независимо. Поэтому версия 0.12 больше версии 0.2.

#Пример порядка версий:

#0.1 < 1.1 < 1.2 < 1.11 < 13.37
#>>> compare_version("0.1", "0.2")
#-1
#>>> compare_version("0.2", "0.1")
#1
#>>> compare_version("4.2", "4.2")
#0
#Подробнее о версиях: http://semver.org/lang/ru/

#Подсказки
#Разобрать строку на части, разделённые некоторой подстрокой, можно так:

#>>> 'foo::bar::baz'.split('::')
#['foo', 'bar', 'baz']

def compare_version(v1, v2):
    c1 = list(map(int, v1.split('.')))
    c2 = list(map(int, v2.split('.')))
    if c1 > c2:
        return 1
    elif c1 < c2:
        return -1
    return 0

#def sign(x):
#    if x > 0:
#        return 1
#   elif x < 0:
#        return -1
#    else:
#        return 0

#def compare_version(first, second):
#    [a1, b1] = first.split('.')
#    [a2, b2] = second.split('.')

#    major = sign(int(a1) - int(a2))
#    minor = sign(int(b1) - int(b2))

#    return major if major != 0 else minor