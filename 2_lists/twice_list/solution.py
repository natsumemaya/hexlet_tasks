#Реализуйте функцию enlarge, которая принимает изображение в виде двумерного списка строк и увеличивает его в два раза, то есть удваивает каждый символ по горизонтали и вертикали.

def show(image):
    for line in image:
        print(line)

dot = ['@']

#>>> show(enlarge(dot))
# @@
# @@
frame = [
    '****',
    '*  *',
    '*  *',
    '****'
     ]
#>>> show(frame)
# ****
# *  *
# *  *
# ****
#>>> show(enlarge(frame))
# ********
# ********
# **    **
# **    **
# **    **
# **    **
# ********
# ********

#Подсказка
#Если вам потребуется склеить список строк в одну строку, воспользуйтесь таким методом:
#>>> chunks = ["Hello", " ", "World", "!"]
#>>> ''.join(chunks)
#'Hello World!'

def enlarge(images):
    result = []
    for items in images:
        new_item = ''
        for item in items:
            new_item += item * 2
        result.append(new_item)
        result.append(new_item)
    return result

#def enlarge(frame):
#    output = []
#    for current_string in frame:
#        modified_string = ''
#        for char in current_string:
#            modified_string += '{}{}'.format(char, char)
#        output.extend([modified_string, modified_string])
#    return output

#def show(image):
#    for line in image:
#        print(line)

#def enlarge(a):
#    A = []
#    for i,x in enumerate(a):
#        c = x.split(' ')
#        for i,x in enumerate(c):
#            c[i] = x*2
#            if c[i] == '':
#                c[i] = x +'  '
#        A.append(' '.join(c))
#        A.append(' '.join(c))
#    return A

#def enlarge(image):
#    output = []
#    for line in image:
#        row = []
#        for pixel in line:
#            # expand horizontally
#            row.extend([pixel, pixel])
#        row = ''.join(row)
#        # expand verticaly
#        output.extend([
#            row,
#            row,
#        ])
#    return output