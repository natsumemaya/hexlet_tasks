# Реализуйте функцию convert, которая принимает на вход список определённой структуры и возвращает словарь, полученный из этого списка.

# Список устроен таким образом, что с помощью него можно представлять словари. Каждый элемент списка — тоже список из двух элементов, где первый элемент — ключ, а второй — значение. Значение тоже может быть списком. Любой список внутри исходного списка всегда рассматривается как данные, которые нужно конвертировать в словарь.

# Примеры
# >>> from solution import convert
# >>> convert([])
# {}
# >>> convert([('key2', 'value2'), ('key', 'value')])
# {'key2': 'value2', 'key': 'value'}
# >>> convert([
# ...   ('key', [('key2', 'anotherValue')]),
# ...   ('key2', 'value2')
# ... ])
# {'key': {'key2': 'anotherValue'}, 'key2': 'value2'}

def to_item(item):
    key, value = item
    return key, convert(value) if isinstance(value, list) else value

def convert(tree):
    return dict(map(to_item, tree))


# def convert(tree):
#     def walk(node, result):
#         for key, walue in node:
#             if isinstance(walue, list):
#                 if walue == []:
#                     result[key] = {}
#                 result[key] = walk(walue, {})
#             else:
#                 result[key] = walue
#         return result
#     return walk(tree, {})

# def convert(tree):
#     result = dict()
#     for key, value in tree:
#         if not isinstance(value, list):
#             result[key] = value
#         else:
#             result[key] = convert(value)
#     return result
