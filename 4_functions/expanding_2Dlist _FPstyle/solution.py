# Увеличение двумерного списка в ФП-стиле
# Это испытание представляет собой задание повышенной сложности. Помните: в самом начале обучения программированию вполне нормально не уметь решать подобные задачи!
# В этом испытании вам предстоит решить ту же проблему, что вы могли решать в испытании "Увеличение двумерного списка" (вам стоит это проделать, если вы ещё не проходили то испытание).
# Задача заключается в том, что нужно реализовать функцию enlarge, которая увеличивает переданное "изображение" в два раза: каждый "пиксель" удваивается по горизонтали и вертикали. Изображением служит список строк, а пиксели в нём — символы строк. Получившаяся функция должна работать так:

# >>> glider = [' * ', '  *', '***']
# >>> def display(image):
# ...     for line in image:
# ...         print(line)
# ...
# >>> display(glider)
#  *
#   *
# ***
# >>> display(enlarge(glider))
#   **
#   **
#     **
#     **
# ******
# ******
# Сама задача не отличается от задачи в оригинальном упражнении, однако в этот раз вам предстоит решить проблему в функциональном стиле!

# Вы не должны использовать изменяемые структуры данных, переменные, циклы и даже рекурсию. Всё, что вы можете делать, это определять функции через композицию существующих!

# Средства для решения задачи
# Вам даны функции-комбинаторы curry и compose, а так же две простые функции pair и dup.

# Функция curry превращает функцию двух аргументов в функцию от первого, возвращающую функцию от второго (такая операция называется каррированием):

# >>> from operator import add
# >>> add(5, 6)
# 11
# >>> f = curry(add)
# >>> f(5)(6)
# 11
# >>> add5 = curry(add)(5)
# >>> add5(10)
# 15
# >>> from functools import reduce
# >>> concat = curry(reduce)(add)
# >>> concat(["Hello", ", ", "World!"])
# "Hello, World!"

# Функция compose берёт одну функцию, затем другую и возвращает их композицию:
# >>> from operator import add, mul
# >>> add5 = curry(add)(5)
# >>> mul3 = curry(mul)(3)
# >>> f = compose(add5)(mul3)   # f(x) == add5(mul3(x))
# >>> g = compose(mul3)(add5)   # f(x) == mul3(add5(x))
# >>> f(1)  # 5 + (3 * 1)
# 8
# >>> g(1)  # 3 * (5 + 1)
# 18
# Оставшиеся две функции элементарны:

# >>> pair = lambda x: [x, x]
# >>> dup = lambda x: x + x
# Ваша задача описать функцию enlarge, через указанные функции и, возможно, map/filter/reduce. Имейте в виду, что задача решаема с использованием одних лишь упомянутых выше функций, не требуются даже lambda-функции!

# Кстати, функция display из первого примера может быть определена и так:

# >>> display = compose(print)(''.join)
# >>> display(['foo', 'bar'])
# foo
# bar
# Линтер закономерно ругается на такие функции, потому что
# обычно именованные функции не делаются с помощью лямбд.
curry = lambda f: lambda x: lambda y: f(x, y)  # noqa: E731
compose = lambda f: lambda g: lambda x: f(g(x))  # noqa: E731

pair = lambda x: [x, x]  # noqa: E731
dup = lambda x: x + x  # noqa: E731

# BEGIN
# Импорты тоже обычно пишутся в начале модуля, но здесь они скрыты
# с целью сохранить интригу :)

from functools import reduce  # noqa: 402
from operator import add # noqa: 402

concat = curry(reduce)(add)
concat_map = compose(compose(concat))(curry(map))

enlarge = concat_map(compose(pair)(concat_map(dup)))
# END

if __name__ == '__main__':
    display = compose(print)('\n'.join)  # noqa: T002
    display(enlarge([
        '+--+',
        '|x |',
        '| o|',
        '+--+',
    ]))

# # BEGIN (write your solution here)
# concat = curry(reduce)(add)
# dup_map = curry(map)(dup)
# concat_dup_map = compose(concat)(dup_map)
# pair_concat_dup_map = compose(pair)(concat_dup_map)
# enlarge = compose(concat)(curry(map)(pair_concat_dup_map))
# # END

# # BEGIN (write your solution here)
# from functools import reduce
# from operator import add


# def enlarge(image):
#     dup_curry = curry(map)(dup)

#     make_line = map(dup_curry, image)
#     make_line_list = map(list, make_line)
#     make_line_whole = map(''.join, make_line_list)
#     make_line_x2 = map(pair, make_line_whole)
#     return reduce(add, make_line_x2)

# # END

# # BEGIN (write your solution here)
# def printer(x):
#     k=list(pair(''.join(list(map(dup,x)))))
#     return k
# def enlarge(glider):
#     k=map(printer,glider)
#     f=lambda s: list(itertools.chain(*s))
#     return f(k)

# # END