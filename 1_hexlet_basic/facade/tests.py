import solution
from solution import numbers1, numbers2, numbers3

attributes = ( # noqa: WPS410
    'power',
    'add',
    'sub',
    'sqrt',
    'mul',
)

def test_names():
    for attribute in attributes:
        if hasattr(solution, attribute):
            continue
        else: 
            raise Exception("not all attributes in __all__!")
    print("test_names ok!")

def test_references():
    if solution.add is numbers2.add2:
        next
    if solution.mul is numbers1.mul1:
        next
    if solution.power is numbers2.power2:
        next
    if solution.sqrt is numbers3.sqrt3:
        next
    if solution.sub is numbers2.sub2:
        print('test_references is ok!')
    else:
        raise Exception('test_references is False!')


def test_all_metavar():
    if 'add' in solution.__all__:
        next
    if 'mul' in solution.__all__:
        next
    if 'power' in solution.__all__:
        next
    if 'sqrt' in solution.__all__:
        next
    if 'sub' in solution.__all__:
        print("test_all_metavar is ok!")
    else:
        print("test_all_metavar is False!")

test_names()
test_references()
test_all_metavar()
