# В данном упражнении необходимо реализовать стековую машину, то есть алгоритм, проводящий вычисления по обратной польской записи.

# Обратная польская нотация или постфиксная нотация — форма записи математических и логических выражений, в которой операнды расположены перед знаками операций. Выражение читается слева направо. Когда в выражении встречается знак операции, выполняется соответствующая операция над двумя ближайшими операндами, находящимися слева от знака операции. Результат операции заменяет в выражении последовательность её операндов и знак, после чего выражение вычисляется дальше по тому же правилу. Таким образом, результатом вычисления всего выражения становится результат последней вычисленной операции.

# Например, выражение (1 + 2) * 4 + 3 в постфиксной нотации будет выглядеть так: 1 2 + 4 * 3 +, а результат вычисления: 15. Другой пример - выражение: 7 - 2 * 3, в постфиксной нотации: 7 2 3 * -, результат: 1.

# solution.py
# Реализуйте функцию rpn_calc, которая принимает список, каждый элемент которого содержит число или знак операции (+, -, *, /). Функция должна вернуть результат вычисления по обратной польской записи.

# Примеры
# >>> rpn_calc([1, 2, '+', 4, '*', 3, '+'])
# 15
# >>> rpn_calc([7, 2, 3, '*', '-'])
# 1
# >>>
import operator

get_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}.get

def rpn_calc(polish):
    stack = []
    for elem in polish:
        op = get_operator(elem)
        if op is not None:
            x = stack.pop()
            y = stack.pop()
            elem = op(y, x)
        stack.append(elem)
    return stack[0]
            
        
# from operator import add, mul, sub, truediv

# def rpn_calc(seq):
#     operation = {'+': add, '-': sub, '*': mul, '/': truediv}
#     operands = []
#     for i in seq:
#         if i in operation:
#             operands.append(operation.get(i)(operands.pop(-2), operands.pop(-1)))
#         else:
#             operands.append(i)
#     return operands[0]
#_________________
# def rpn_calc(args):
#     stack = []
#     for arg in args:
#         if str(arg) in '+-*/':
#             b = stack.pop()
#             a = stack.pop()
#             stack.append(calc(arg, a, b))
#         else:
#             stack.append(arg)

#     return stack[0]


# def calc(op, a, b):
#     if op == '+':
#         return a + b
#     if op == '-':
#         return a - b
#     if op == '*':
#         return a * b
#     if op == '/':
#         return a / b