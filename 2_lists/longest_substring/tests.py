from solution import find_longest_length


def test_find_length_length():
    assert find_longest_length('') == 0
    assert find_longest_length('a') == 1
    assert find_longest_length('jabjcdel') == 7
    assert find_longest_length('abcddef') == 4
    assert find_longest_length('abbccddeffg') == 3
    assert find_longest_length('abcd') == 4
    assert find_longest_length('1234561qweqwer') == 9
    print('test_find_length_length is Ok!')

test_find_length_length()
