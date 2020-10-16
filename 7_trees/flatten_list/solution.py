# Реализуйте функцию flatten, которая делает плоским вложенный список.

# Примеры
# >>> from solution import flatten
# >>> flatten([])
# []
# >>> flatten([2, [3, 5], [[4, 3], 2]])
# [2, 3, 5, 4, 3, 2]
# >>>

def flatten(lst):
    result = []
    for item in lst:
        if type(item) != list:
            result.append(item)
        else:
            result.extend(flatten(item))    
    return result

# def normalize(item):
#     return flatten(item) if isinstance(item, list) else [item]

# def flatten(tree):
#     return sum(map(normalize, tree), [])

## Этот вариант будет эффективнее из-за того, что не создаёт промежуточные
## структуры, а вместо этого использует мутабельный объект.
#  def flatten(tree):
#      result = []

#      def walk(subtree):
#          for item in subtree:
#              if isinstance(item, list):
#                  walk(item)
#              else:
#                  result.append(item)
#      walk(tree)
#      return result