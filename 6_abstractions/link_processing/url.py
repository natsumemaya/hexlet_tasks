# src/url.py
# Реализуйте абстракцию для работы с URL. Она должна извлекать и менять части адреса.

# Интерфейс:

# make(url) - Конструктор. Создает URL.
# get_scheme(data) - Селектор (геттер). Извлекает схему.
# set_scheme(data, scheme) - Сеттер. Меняет схему.
# get_host(data) - Геттер. Извлекает host.
# set_host(data, host) - Сеттер. Меняет host.
# get_path(data) - Геттер. Извлекает путь.
# set_path(data, path) - Сеттер. Меняет путь.
# get_query_param(data, param_name, default=None) - Геттер. Извлекает значение для параметра запроса. Третьим параметром функция принимает значение по умолчанию, которое возвращается тогда, когда в запросе не было такого параметра
# set_query_param(data, key, value) - Сеттер. Устанавливает значение для параметра запроса. Если передано значение None, то параметр отбрасывается.
# to_string(data) - Геттер. Преобразует URL в строковой вид.
# Все сеттеры должны возвращать новый изменённый URL, а старый оставлять неизменным.

# Примеры
# >>> import url
# >>> u = url.make('https://hexlet.io/community?q=low')
# >>>
# >>> u = url.set_scheme(u, 'http')
# >>> url.to_string(u)
# 'http://hexlet.io/community?q=low'
# >>>
# >>> u = url.set_path(u, '/404')
# >>> url.to_string(u)
# 'http://hexlet.io/404?q=low'
# >>>
# >>> url.get_query_param(u, 'q')
# 'low'
# >>>
# >>> u = url.set_query_param(u, 'page', 5)
# >>> url.to_string(u)
# 'http://hexlet.io/404?q=low&page=5'
# >>>
# >>> u = url.set_query_param(u, 'q', 'high')
# >>> url.to_string(u)
# 'http://hexlet.io/404?q=high&page=5'
# >>>
# >>> u = url.set_query_param(u, 'q', None)
# >>> url.to_string(u)
# 'http://hexlet.io/404?page=5'
# Подсказки
# Парсинг URL — urllib.parse.urlparse
# Парсинг параметров запроса — urllib.parse.parse_qs
# Формирование строки с параметрами запроса — urllib.parse.urlencode
# Сборка конечного URL — urllib.parse.urlunparse
# urlparse возвращает иммутабельный объект типа namedtuple. Получить копию такого объекта с одним изменённым значением можно с помощью метода _replace.

from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


def make(url):
    """Make an URL representation from string."""
    return urlparse(url)


def get_scheme(data):
    """Return a scheme of given URL."""
    return data.scheme


def set_scheme(data, scheme):
    """Return a new URL with replaced host."""
    return data._replace(scheme=scheme)  # noqa: WPS437


def get_host(data):
    """Return a host of given URL."""
    return data.netloc


def set_host(data, host):
    """Return a new URL with replaced host."""
    return data._replace(netloc=host)  # noqa: WPS437


def get_path(data):
    """Replace scheme of given URL."""
    return data.path


def set_path(data, path):
    """Return a new URL with replaced path."""
    return data._replace(path=path)  # noqa: WPS437


def get_query_param(data, key, default=None):
    """
    Return a value of named query parameter of given URL.

    Function returns default value if named parameter is not present.
    """
    return parse_qs(data.query).get(key, [default])[0]


def set_query_param(data, key, value):
    """Return a new URL with replaced query parameter."""
    params = parse_qs(data.query)
    if value is None:
        params.pop(key, None)
    else:
        params[key] = value
    return data._replace(query=urlencode(params, doseq=True))  # noqa: WPS437


def to_string(data):
    """Return a string representation of given URL."""
    return urlunparse(data)