# Вам нужно реализовать класс TreeBuilder. Этот класс призван давать возможность собирать древовидные структуры пошагово. Метод add добавляет "лист" в текущий узел дерева:

# >>> tree = TreeBuilder()
# >>> tree.add('1st')
# Свойство structure возвращает текущую структуру дерева:

# >>> tree.structure
# ['1st']
# А использование экземпляра в качестве менеджера контекста добавляет вложенный узел дерева, делая его текущим в рамках контекста. При этом "спускаться вниз" можно на произвольную глубину:

# >>> with tree:
# ...     tree.add('2nd')
# ...     with tree:
# ...         tree.add('3rd')
# ...     tree.add('4th')
# ...
# >>> tree.structure
# ['1st', ['2nd', ['3rd'], '4th']]
# Если в рамках контекста не было добавлено ни одного "листа", то весь узел не должен появляться в итоговой структуре:

# >>> tree.structure
# ['1st', ['2nd', ['3rd'], '4th']]
# >>> with tree:
# ...     pass
# ...
# >>> tree.structure
# ['1st', ['2nd', ['3rd'], '4th']]  # пустой список не был добавлен!
# Структура дерева выводится в виде вложенных списков.

# Пример целиком
# >>> tree = TreeBuilder()
# >>> tree.structure
# []
# >>> tree.add('1st')
# >>> tree.structure
# ['1st']
# >>> with tree:
# ...     tree.add('2nd')
# ...     with tree:
# ...         tree.add('3rd')
# ...     tree.add('4th')
# ...     with tree:
# ...         pass
# ...
# >>> tree.structure
# ['1st', ['2nd', ['3rd'], '4th']]

class TreeBuilder(object):
    """Сборщик деревьев, работающий в виде менеждера контекста."""

    # BEGIN
    def __init__(self):
        """Инициализирует экземпляр сборщика."""
        self._stack = ([],)

    def __enter__(self):
        """Создаёт новый контекст."""
        self._stack = ([], self._stack)
        return self

    def __exit__(self, exception, *args):
        """Осуществляет выход из текущего контекста."""
        if exception is None:
            head, tail = self._stack
            if head:
                tail[0].append(head)
            self._stack = tail
    # END

    def add(self, value):
        """Добавляет в значение в текущую позицию в дереве."""
        # BEGIN
        self._stack[0].append(value)
        # END

    @property
    def structure(self):
        """
        Возвращает текущую структуру дерева в виде вложенных списков.

        Returns:
            Список списков вида [1, [2, 3, [4], 5], 6, [7, 8]]

        """
        # BEGIN
        return self._stack[0]
        # END
