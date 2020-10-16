# Реализуйте и экспортируйте функции ip2int и int2ip, которые преобразовывают представление IP-адреса из десятичного формата с точками в 32-битное число в десятичной форме и обратно.

# Функция ip2int принимает на вход строку и должна возвращать число. А функция int2ip наоборот: принимает на вход число, а возвращает строку.

# Примеры
# >>> ip2int('128.32.10.1')
# 2149583361
# >>> ip2int('0.0.0.0')
# 0
# >>> ip2int('255.255.255.255')
# 4294967295
# >>>
# >>> int2ip(2149583361)
# '128.32.10.1'
# >>> int2ip(0)
# '0.0.0.0'
# >>> int2ip(4294967295)
# '255.255.255.255'
# Подсказки
# IPv4

from functools import reduce

POWERS_OF_TWO = (2 ** 24, 2 ** 16, 2 ** 8, 2 ** 0)  # noqa: WPS221


def ip2int(ip):
    return sum(map(
        lambda x, y: int(x) * y,
        ip.split('.'),
        POWERS_OF_TWO,
    ))


def _make_octet(accumulator, divider):
    ip, remainder = accumulator
    octet, new_remainder = divmod(remainder, divider)
    return ip + (str(octet),), new_remainder


def int2ip(integer):
    octets, _ = reduce(_make_octet, POWERS_OF_TWO, ((), integer))
    return '.'.join(octets)


# from ipaddress import ip_address

# def ip2int(ip):
#     reversed_ip_octet = list(map(
#         lambda octet: int(octet),
#         reversed(ip.split('.')),
#     ))
#     buffer = []
#     for index, octet in enumerate(reversed_ip_octet):
#         buffer.append(octet * 256 ** index)
#     return sum(buffer)

# def int2ip(number):
#     return str(ip_address(number))


# from functools import reduce

# def ip2int(ip_address):
#     return reduce(lambda a, b: int(a) * 256 + int(b), ip_address.split('.'))

# def int2ip(int_value):
#     return '.'.join([str(int(int_value / 256 ** i) % 256) for i in [3, 2, 1, 0]])