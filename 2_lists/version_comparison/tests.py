from solution import compare_version

def test_compare():
    versions = [('0.1', '0.2'), ('0.2', '0.1'), ('4.2', '4.2'), ('0.2', '0.12'), ('3.2', '4.12'), ('3.2', '2.12')]
    answers = [-1, 1, 0, -1, -1, 1]
    results = []
    for version in versions:
        x, y = version
        results.append(compare_version(x, y))
    for i in range(len(answers)):
        if answers[i] == results[i]:
            next
        else:
            raise Exception(f'test_compare is Failed! For {repr(versions[i])} has answer > {results[i]}')
    print('test_compare is Ok!')

test_compare()