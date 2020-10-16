import solution

def check(a, b, expected):
    result = solution.binary_sum(a, b)
    answer = bin(expected)[2:]
    return result, answer, result == answer

args = [ ('1000', '10', 0b1000 + 0b10),
('1010', '101', 0b1010 + 0b101),
('1', '1', 0b1 + 0b1),
('1111', '1111', 0b1111 + 0b1111)
]

for arg in args:
    a, b, ex = arg
    print(check(a, b, ex))