from solution import decode

def test_decode():
    assert decode('') == ''
    assert decode('|¯') == '1'
    assert decode('_') == '0'
    assert decode('_|¯|____|¯|__|¯¯¯') == '011000110100'
    assert decode('|¯|___|¯¯¯¯¯|___|¯|_|¯') == '110010000100111'
    assert decode('¯|___|¯¯¯¯¯|___|¯|_|¯') == '010010000100111'
    print('test_decode is Ok!')

test_decode()

# from re import compile, sub

# def decode(seq):
#     one = compile(r"(\|¯|\|_)")
#     zero = compile(r"(\||¯|_)")
#     str_with_one = sub(one, '1', seq)
#     return sub(zero, '0', str_with_one)
#_________________
# def cleaning(list_):
#     result = []
#     for index, element in enumerate(list_):
#         if list_[index - 1] == 1:
#             continue
#         result.append(str(element))
#     return result


# def decode(string):
#     signal = {'_': 0, '|': 1, '¯': 0}
#     converted_list = list(map(lambda x: signal[x], string))
#     return ''.join(cleaning(converted_list))

# def decode(nrzi_code):
#     result = ''
#     flag = False
#     for symbol in nrzi_code:
#         if flag:
#             flag = False
#         else:
#             if symbol == '|':
#                 result += '1'
#                 flag = True
#             else:
#                 result += '0'
#     return result

# def decode(signal):
#     signal = signal.replace('|_', '1').replace('|¯', '1')
#     return signal.replace('¯', '0').replace('_', '0')

# def decode(code):
#     decode = []
#     a = 0
#     for i in code:
#         if a == 0:
#             if i == '_' or i == '¯':
#                 decode.append('0')
#             elif i == '|':
#                 a = 1
#         else: 
#             if i == '_' or i == '¯':
#                 decode.append('1')
#                 a = 0
#     return ''.join(decode)