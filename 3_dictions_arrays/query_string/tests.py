from solution import build_query_string 


def test_build_query_string():
    assert build_query_string({}) == ''
    assert build_query_string({'page': 1}) == 'page=1'
    assert build_query_string({'per': 10, 'page': 1}) == 'page=1&per=10'
    assert build_query_string(
        {
            'a': 10,
            's': 'Wow',
            'd': 3.2,
            'z': '89',
        },
    ) == 'a=10&d=3.2&s=Wow&z=89'
    print('test_build_query_string is Ok!')

test_build_query_string()