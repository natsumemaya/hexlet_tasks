# Реализуйте функцию merged, которая объединяет несколько словарей в один общий словарь. Функция принимает любое количество аргументов и возвращает результат в виде словаря, в котором каждый ключ содержит множество (set) уникальных значений.

# Примеры
# >>> from solution import merged
# >>> merged({}, {}) == {}
# True
# >>> merged(
# ...     {'a': 1, 'b': 2},
# ...     {'b': 10, 'c': 100}
# ... ) == {'a': {1}, 'b': {2, 10}, 'c': {100}}
# ...
# True
# >>>
# Подсказка
# Функция может вернуть любой подобный словарю объект. Вы можете выбрать наиболее подходящий среди имеющихся в стандартной библиотеке.

from collections import defaultdict

def merged(*dicts):
    aggregate = defaultdict(set)
    for source in dicts:
        for key, value in source.items():
            aggregate[key].add(value)
    return aggregate

