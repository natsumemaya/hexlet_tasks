# В данном испытании мы будем использовать двоичное дерево, и выполнять агрегацию данных.

# src/solution.py
# Реализуйте следующие методы в классе solution.Node:

# __len__() — возвращает количество узлов в дереве (используется в len()).
# __repr__() — возвращает строковое представление дерева (используется для отображения в REPL).
# total() — возвращает сумму всех ключей дерева.
# minimum() — возвращает минимальный ключ дерева.
# maximum() — возвращает максимальный ключ дерева.
# to_list() — возвращает плоский список, содержащий все ключи.
# every(fn) — проверяет, удовлетворяют ли все ключи дерева условию, заданному в передаваемой функции.
# some(fn) — проверяет, удовлетворяет ли какой-либо ключ дерева условию, заданному в передаваемой функции.
# При обходе дерева нужно использовать порядок слева-направо. То есть вначале обрабатываем ключ узла, затем ключ левого ребёнка, после чего ключ правого ребёнка.

# Примеры
# >>> from solution import Node
# >>> tree = Node(
# ...    9,
# ...    Node(
# ...       4,
# ...       Node(8),
# ...       Node(
# ...          6,
# ...          Node(3),
# ...          Node(7),
# ...       ),
# ...    ),
# ...    Node(
# ...       17,
# ...       right=Node(
# ...          22,
# ...          Node(20),
# ...       ),
# ...    ),
# ... )
# >>> len(tree)
# 9
# >>> tree.total()
# 96
# >>> tree.to_list()
# [9, 4, 8, 6, 3, 7, 17, 22, 20]
# >>> tree.every(lambda key: key <= 22)
# True
# >>> tree.some(lambda key: key > 22)
# False
# >>> tree.minimum()
# 3
# >>> tree.maximum()
# 22
# >>> tree2 = Node(3, Node(1), Node(2))
# >>> tree2  # выводится repr(tree2)
# Node(3, Node(1, None, None), Node(2, None, None))
# >>>

# Подсказки
# Для реализации каждого из методов потребуется выполнить обход всех узлов дерева.

import operator


class Node(object):  # noqa: WPS214

    def __init__(self, key, left=None, right=None):
        """Create a new tree node."""
        self.key = key
        self.left = left
        self.right = right

# BEGIN
    def fold(self, combine, make):
        result = make(self.key)
        if self.left is not None:
            result = combine(
                result,
                self.left.fold(combine, make),
            )
        if self.right is not None:
            result = combine(
                result,
                self.right.fold(combine, make),
            )
        return result

    def __len__(self):
        """Return a total count of tree nodes."""
        return self.fold(operator.add, lambda _: 1)

    def total(self):
        return self.fold(operator.add, lambda x: x)

    def to_list(self):
        return self.fold(operator.add, lambda x: [x])

    def some(self, pred):
        return self.fold(operator.or_, pred)

    def every(self, pred):
        return self.fold(operator.and_, pred)

    def minimum(self):
        return self.fold(min, lambda x: x)

    def maximum(self):
        return self.fold(max, lambda x: x)

    def __repr__(self):
        """Return text representation of the tree."""
        return '{cls}({key}, {left}, {right})'.format(
            cls=self.__class__.__name__,
            key=self.key,
            left=repr(self.left),
            right=repr(self.right),
        )
