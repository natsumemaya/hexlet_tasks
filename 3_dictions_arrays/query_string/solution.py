# Query String (строка запроса) — часть URL, содержащая константы и их значения. Она начинается после вопросительного знака и идет до конца адреса. Пример:
# # query string: page=5
# https://ru.hexlet.io/blog?page=5
# Если параметров несколько, то они отделяются амперсандом &
# # query string: page=5&per=10
# https://ru.hexlet.io/blog?per=10&page=5
# 'src/solution.py'
# Напишите функцию build_query_string, которая принимает на вход словарь с параметрами и возвращает строку запроса, сформированную из этих параметров.
# Пример
# >>> build_query_string({'per': 10, 'page': 1})
# 'page=1&per=10'
# Подсказки
# Тесты ожидают, что параметры будут отсортированы, поэтому воспользуйтесь функцией sorted.
# Чтобы собрать строку из нескольких кусков с помощью некоторого разделителя, вы можете воспользоваться таким способом:
# >>> ','.join(['abc', 'cde', 'def'])
# 'abc,cde,def'

def build_query_string(params):
    items = []
    for key, value in sorted(params.items()):
        items.append('{}={}'.format(key, value))
    return '&'.join(items)