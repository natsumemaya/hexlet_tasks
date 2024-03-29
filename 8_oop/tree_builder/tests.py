from solution import TreeBuilder


def test_tree_builder():
    tree = TreeBuilder()
    tree.add('root')
    with tree:
        tree.add('first child')
        tree.add('second child')
        with tree:
            tree.add('grandchild')
        tree.add('bastard')
        with tree:  # noqa: WPS328, this subtree is empty intentionally
            pass    # noqa: WPS420, we need to do nothing
        tree.add('another bastard')

    assert tree.structure == [
        'root',
        [
            'first child',
            'second child',
            ['grandchild'],
            'bastard',
            'another bastard',
        ],
    ]
    print('test_tree_builder is Ok!')

test_tree_builder()


# class TreeBuilder(object):
#     def __init__(self, initial_structure=None):
#         if initial_structure is None:
#             initial_structure = []
#         self.structure = initial_structure
#         self._target_for_add = self

#     @property  # getter
#     def structure(self):
#         return self._structure

#     @structure.setter
#     def structure(self, value):
#         self._structure = value

#     def add(self, leaf_value):
#         """Add to the current node."""
#         self._target_for_add.append(leaf_value)

#     def append(self, leaf_value):
#         """Add to base level."""
#         self._structure.append(leaf_value)

#     def __enter__(self):
#         self._target_for_add = TreeBuilder.Node(self._target_for_add)

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self._target_for_add:
#             self._target_for_add.parent.append(self._target_for_add)
#         self._target_for_add = self._target_for_add.parent

#     class Node(list):
#         def __init__(self, parent, *args):
#             self.parent = parent
#             initial_value = list(args)
#             self.extend(initial_value)
