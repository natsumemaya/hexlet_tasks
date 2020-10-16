# Реализуйте функцию find_where, которая принимает на вход список книг и поисковый запрос и возвращает первую книгу, которая соответствует запросу. Каждая книга в списке — это словарь, содержащий её параметры, поисковый запрос — тоже словарь с параметрами.

# Если совпадений не было, то функция должна вернуть None.

# >>> books = [
# ...     {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
# ...     {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
# ...     {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
# ...     {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
# ...     {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
# ...     {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
# ... ]
# ...
# >>> find_where(books, {'author': 'Shakespeare', 'year': 1611})
# {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611}

def find_where(items, search_request):
    # Значение object() в качестве умолчательного используется для того,
    # чтобы не получилось получить от get значение None и случайно
    # успешно сравнить с value == None.
    # Каждое значение object() всегда равно только самому себе.
    default = object()
    for item in items:
        for key, value in search_request.items():
            # Здесь можно было бы использовать
            # что-то вроде "key in book and book[key] !=..." и обойтись
            # без всяких object(). Но хочется обращаться по ключу
            # ровно один раз!
            if item.get(key, default) != value:
                break
        else:
            return item

# МОЕ
# def find_where(dicts, book):
#   for item in dicts:
#     a = set(book.values())
#     b = set(item.values())
    
#     if a.issubset(b):
#       return item

# def find_where(books, query_search):
#     default = object()
#     for book in books:
#         for key, value in query_search.items():
#             if book.get(key, default) != value:
#                 break
#         else:
#             return book
#     return None
