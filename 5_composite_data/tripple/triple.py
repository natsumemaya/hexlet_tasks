# Кроме пар можно создавать абстрактные типы данных, которые содержат внутри себя три и более элемента.
# В данном испытании необходимо реализовать структуру данных тройка, позволяющую хранить три значения. Как и в случае с парами создаётся конструктор make и селекторы get1, get2, get3, которые будут извлекать соответствующие значения.

# triple.py
# Реализуйте и экспортируйте следующие функции:
# * make
# * get1
# * get2
# * get3

# Пример
# >>> triple = make(3, 5, 'I am element from triple')
# >>>
# >>> get1(triple)
# 3
# >>> get2(triple)
# 5
# >>> get3(triple)
# I am element from triple
def cons(a, b):
    def f(message):
        if message == "car":
            return a
        if message == "cdr":
            return b
    return f

def car(pair):
    return pair("car")

def cdr(pair):
    return pair("cdr")


def make(x, y, z):
    return cons(cons(x, y), z) 

def get1(point):
    return car(car(point))

def get2(point):
    return cdr(car(point))

def get3(point):
    return cdr(point)

# def make(a, b, c):
#     def f(message):
#         if message == "get1":
#             return a
#         if message == "get2":
#             return b
#         if message == "get3":
#             return c
#     return f

# def get1(triple):
#     return triple("get1")

# def get2(triple):
#     return triple("get2")

# def get3(triple):
#     return triple("get3")

# _____________________
# def make(el1, el2, el3):
#     return (el1, el2, el3)

# def get1(triple):
#     return triple[0]

# def get2(triple):
#     return triple[1]

# def get3(triple):
#     return triple[2]