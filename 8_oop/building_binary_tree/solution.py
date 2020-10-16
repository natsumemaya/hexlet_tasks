# Построение двоичного дерева
# Двоичное дерево — иерархическая структура данных, в которой каждый узел имеет не более двух потомков (детей). Как правило, первый называется родительским узлом, а дети называются левым и правым наследниками.

# В данном испытании мы будем использовать подвид двоичного дерева — двоичное дерево поиска. Правильное дерево не содержит повторяющихся ключей, и для каждого узла гарантируется, что в левом поддереве все значения меньше текущего, а в правом — больше.

# Реализуйте класс, который представляет собой узел дерева.

# Класс должен содержать:

# Атрибут key — ключ узла.
# Атрибуты left и right — ссылки на левого и правого ребёнка соответственно. Если ребёнок в узле отсутствует, геттер возвращает None.
# Метод insert(key) — выполняет добавление узла, формируя правильное двоичное дерево.
# Примеры
# >>> from solution import Node
# >>> tree = Node()
# >>> tree.insert(9)
# >>> tree.insert(17)
# >>> tree.insert(4)
# >>> tree.insert(3)
# >>> tree.insert(6)
# >>> tree.key
# 9
# >>> tree.left.key
# 4
# >>> tree.right.key
# 17
# >>> tree.left.left.key
# 3
# >>> tree.left.right.key
# 6
# >>>

class Node(object):
    def __init__(self):
        """Create an empty tree."""
        self.key = None
        self.left = None
        self.right = None

    def insert(self, key):
        if self.key is None:
            self.key = key
            return
        if key == self.key:
            return
        if key < self.key:
            if not self.left:
                self.left = self.__class__()
            target = self.left
        else:
            if not self.right:
                self.right = self.__class__()
            target = self.right
        target.insert(key)