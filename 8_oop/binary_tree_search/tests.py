from solution import Node


def test_single_node():
    single_node = Node(1)
    assert single_node.key == 1
    assert single_node.left is None
    assert single_node.right is None
    print('test_single_node is Ok!')


def test_search():
    node5 = Node(5)
    node22 = Node(22, right=Node(20))
    tree = Node(
        9,
        Node(
            4,
            Node(3),
            Node(
                6,
                node5,
                Node(7),
            ),
        ),
        Node(
            17,
            right=node22,
        ),
    )

    assert tree.search(5) is node5
    assert tree.search(22) is node22
    assert tree.search(35) is None
    assert tree.search(2) is None
    print('test_search is Ok!')


def test_search_in_bad_tree():
    tree = Node(
        9,
        Node(
            4,
            Node(
                6,
                Node(5),
                Node(7),
            ),
            Node(3),
        ),
        Node(
            17,
            right=Node(22),
        ),
    )

    assert tree.search(5) is None
    assert tree.search(7) is None
    assert tree.search(6) is None
    assert tree.search(4).key == 4
    assert tree.search(22).key == 22
    print('test_search_in_bad_tree is Ok!')

test_single_node()
test_search()
test_search_in_bad_tree()