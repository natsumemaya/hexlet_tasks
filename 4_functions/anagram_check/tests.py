from itertools import permutations

from solution import filter_anagrams


def test_filter_anagrams_with_strings():
    empty = ''
    assert list(filter_anagrams(empty, [empty, 'foo', empty])) == [empty, empty]

    assert list(filter_anagrams('laser', ['lazing', 'lazy', 'lacer'])) == []

    assert list(filter_anagrams(
        'abba', ['aabb', 'abcd', 'bbaa', 'dada'],
    )) == ['aabb', 'bbaa']

    assert list(filter_anagrams(
        'racer', ['crazer', 'carer', 'racar', 'caers', 'racer'],
    )) == ['carer', 'racer']
    print('test_filter_anagrams_with_strings is Ok!')


def test_filter_anagrams_with_tuples():
    assert list(filter_anagrams((), [(), ()])) == [(), ()]

    tri = (1, 2, 3)
    irt = tuple(reversed(tri))
    assert list(filter_anagrams(
        tri, [tri, irt, tri + (4,)],
    )) == [tri, irt]
    print('test_filter_anagrams_with_tuples is Ok!')


def test_filter_anagrams_with_false_anagrams():
    assert list(filter_anagrams('bob', ['boo', 'bo', 'obbo'])) == []
    print('test_filter_anagrams_with_false_anagrams is Ok!')


def test_filter_anagrams_with_permutations():
    sample = tuple('abcd')
    sample_permutations = list(permutations(sample))
    # ^ [('a', 'b', 'c', 'd'), ('a', 'b', 'd', 'c'), ...
    # ...('d', 'c', 'a', 'b'), ('d', 'c', 'b', 'a')]
    assert len(list(filter_anagrams(
        sample, sample_permutations,
    ))) == len(sample_permutations)
    print('test_filter_anagrams_with_permutations is Ok!')

test_filter_anagrams_with_strings()
test_filter_anagrams_with_tuples()
test_filter_anagrams_with_false_anagrams()
test_filter_anagrams_with_permutations()