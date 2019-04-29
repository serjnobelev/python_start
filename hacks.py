# Unpacking
# обычно используется когда из функции нужно вернуть больше чем 1 результат

# s, k = (1, 2)
# print(k)

# s, k = [1, 2]
# print(s, k)

# s, *k = [1, 2, 3, 4]
# print(s, k)

# first, *str = 'my str'
# print(str)

# def my_fnc():
#     x1 = 1
#     x2 = 2
#     return (x1, x2)
#
# v1, v2 = my_fnc()
# print(v1, v2)

def accepted_args(*args):
    print(type(args))
    print(args)
    print(sum(args))

accepted_args(1, 2, 3)

values = [1, 2 ,3]
# accepted_args(values)

# Convert list to tuple
accepted_args(*values)

# kwargs is the same

def fnc_kwargs(**kwargs):
    print(kwargs)

my_dict = {'day': 'wed', 'month': 'jan'}

# Convert dict to kwargs
fnc_kwargs(**my_dict)