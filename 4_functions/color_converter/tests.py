from solution import rgb2hex


def test_compose():
    assert rgb2hex(0, 0, 0) == '#000000'
    assert rgb2hex(255, 255, 255) == '#ffffff'
    assert rgb2hex(0, 132, 12) == '#00840c'
    assert rgb2hex(36, 171, 0) == '#24ab00'
    assert rgb2hex(r=84, g=63, b=171) == '#543fab'
    assert rgb2hex(r=247, b=222, g=0) == '#f700de'
    assert rgb2hex(r=198, g=1, b=35) == '#c60123'
    print('test_compose is Ok!')

test_compose()

# def rgb2hex(r=0, g=0, b=0):
#     hex_ = map(lambda x: hex(x).split('x')[-1], [r, g, b])
#     format_ = map(lambda x: '0{}'.format(x) if len(x) == 1 else x, hex_)
#     return '#{}'.format(''.join(format_))

# def rgb2hex(r=None, g=None, b=None):
#     result = ['#']
#     for i in (r, g ,b):
#         if len(hex(i)) == 3: 
#             result.append('0')
#             result.append(hex(i)[2:])
#         else: 
#             result.append(hex(i)[2:])
#     return ''.join(result)

# def rgb2hex(r, g, b):
#     return '#{:02x}{:02x}{:02x}'.format(r, g, b)
