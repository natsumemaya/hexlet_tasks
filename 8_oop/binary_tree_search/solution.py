# Двоичное дерево поиска состоит из узлов, каждый из которых содержит значение ключа и два поддерева (левое и правое), которые в свою очередь также являются двоичными деревьями. Правильное дерево не содержит повторяющихся ключей, и для каждого узла гарантируется, что в левом поддереве все значения меньше текущего, а в правом — больше.

# Реализуйте класс, который реализует представление узла. При инициализации объекта класс принимает на вход три параметра:

# key — значение ключа (число),
# left — левое поддерево (тоже узел, по умолчанию None),
# right — правое поддерево (по умолчанию None).
# Каждый экземпляр класса должен содержать атрибуты:

# key
# left
# right
# Также класс должен реализовывать метод search(key), который выполняет поиск узла в правильно построенном двоичном дереве по ключу и возвращает узел. Если узел не найден, возвращается None.

# Примеры
# >>> from solution import Node
# >>> node5 = Node(5)
# >>> node22 = Node(22, right=Node(20))
# >>> tree = Node(
# ...     9,
# ...     Node(
# ...         4,
# ...         Node(3),
# ...         Node(
# ...             6,
# ...             node5,
# ...             Node(7),
# ...         ),
# ...     ),
# ...     Node(
# ...         17,
# ...         right=node22,
# ...     ),
# ... )
# >>> tree.search(6).key
# 6
# >>> tree.search(6).left.key
# 5
# >>> tree.search(6).right.key
# 7
# >>> tree.search(5) is node5
# True
# >>> tree.left.left.key
# 3
# >>>

class Node(object):
    def __init__(self, key, left=None, right=None):
        """Create a node of binary search tree."""
        self.key = key
        self.left = left
        self.right = right

    def search(self, key):
        """Search a value in tree.

        Returns:
            Found node or None.

        """
        if key == self.key:
            return self
        elif key < self.key and self.left:
            return self.left.search(key)
        elif key > self.key and self.right:
            return self.right.search(key)

# class Node:
#     def __init__(self, key, left=None, right=None):
#         self.key = key
#         self.left = left
#         self.right = right

#     def search(self, key):
#         if key == self.key:
#             return self

#         child_node = self.left if key < self.key else self.right

#         if child_node is not None:
#             return child_node.search(key)