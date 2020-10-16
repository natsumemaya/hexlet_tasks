from solution import find_where

TITLE, AUTHOR, YEAR = 'title', 'author', 'year'
BOOKS = (
    {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111},
    {TITLE: 'Cymbeline', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'The Tempest', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'Book of Foos Barrrs', AUTHOR: 'FooBar', YEAR: 2222},
    {TITLE: 'Still foooing', AUTHOR: 'FooBar', YEAR: 333},
    {TITLE: 'Happy Foo', AUTHOR: 'FooBar', YEAR: 4444},
)


def test_find_where():
    assert find_where(BOOKS, {}) == BOOKS[0]

    assert find_where(BOOKS, {AUTHOR: 'Pushkin'}) is None

    assert find_where(BOOKS, {YEAR: 1111, AUTHOR: 'Pushkin'}) is None

    assert find_where(BOOKS, {"genre": 'Thriller'}) is None

    assert find_where(
        BOOKS, {YEAR: 1111},
    ) == {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111}

    assert find_where(
        BOOKS, {AUTHOR: 'Shakespeare', YEAR: 1611},
    )[TITLE] == 'Cymbeline'

    assert find_where(BOOKS, BOOKS[2]) == BOOKS[2]
    print('test_find_where is Ok!')

test_find_where()
