# Реализуйте функцию-предикат is_valid_ipv6, которая проверяет IPv6-адреса (адреса шестой версии интернет протокола) на корректность. Функция принимает на вход строку с адресом IPv6 и возвращает True, если адрес корректный, и False, если нет.

# Дополнительные условия:

# Работа функции не зависит от регистра символов.
# Ведущие нули в группах цифр необязательны.
# Самая длинная последовательность групп нулей, например, :0:0:0: может быть заменена на два двоеточия ::. Такую замену можно произвести только один раз.
# Одна группа нулей :0: не может быть заменена на ::.
# Примеры
# >>> from solution import is_valid_ipv6
# >>> is_valid_ipv6('10:d3:2d06:24:400c:5ee0:be:3d')
# True
# >>> is_valid_ipv6('::1')
# True
# >>> is_valid_ipv6('2607:G8B0:4010:801::1004')
# False
# >>> is_valid_ipv6('2.001::')
# False
# >>> 
# Подсказки
# IPv6
# Для реализации проверки пограничных случаев изучите список IP-адресов в модуле с тестами.

def is_valid_group(group):
    if len(group) > 4:
        return False
    # Handle the error
    # https://docs.python.org/3/tutorial/errors.html
    try:
        decimal = int(group, 16)
    except ValueError:
        return False
    return decimal < 2 ** 16


def is_valid_ipv6(ipv6):
    if ipv6.count('::') > 1:
        return False

    groups = []

    for group in filter(None, ipv6.split('::')):
        groups.extend(group.split(':'))

    is_full = '::' not in ipv6
    length = len(groups) if is_full else len(groups) + 2
    if length > 8 or (is_full and length < 8):
        return False

    return False not in map(is_valid_group, groups)

# from ipaddress import AddressValueError, IPv6Address

# def is_valid_ipv6(ip):
#     try:
#         IPv6Address(ip)
#     except AddressValueError:
#         return False
#     return True

# import socket

# def is_valid_ipv6(ip: str) -> bool:
#     try:
#         socket.inet_pton(socket.AF_INET6, ip)
#     except socket.error:
#         return False
#     return True

# def is_valid_ipv6(source):
#     answer = 0
#     correct_members = [
#         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#         'a', 'A', 'b', 'B', 'c', 'C',
#         'D', 'd', 'E', 'e', 'F', 'f', ':',
#     ]
#     for member in source:
#         if member not in correct_members:
#             answer = 1
#     my_list = source.split(":")
#     length = len(my_list)
#     if length > 8:
#         answer = 1
#     if length > 7 and my_list.count('') > 0:
#         answer = 1
#     for i in my_list:
#         if len(i) > 4:
#             answer = 1
#     if length < 8 and my_list.count('') < 1:
#         answer = 1
#     check = 0
#     number_of_double_double_points = 0
#     while check != len(source):
#         if check < (len(source) - 1):
#             if source[check] == ':' and source[check + 1] == ':':
#                 number_of_double_double_points += 1
#                 if number_of_double_double_points > 1:
#                     answer = 1
#         check += 1
#     first_symbol = source[0]
#     second_symbol = source[1]
#     last_symbol = source[-1]
#     pre_last_symbol = source[-2]
#     if first_symbol == ':' and second_symbol != ':':
#         answer = 1
#     if last_symbol == ':' and pre_last_symbol != ':':
#         answer = 1
#     return answer != 1