l = []

# l.append(0)
# l.append('string')
#
# def test(inp):
#     if inp == 1:
#         return 10
#     else:
#         return 0
#
# # l.append(test)
#
# def new_func(some_func, digit):
#     res = some_func(digit)
#     print(res)
#
# print(max(5, 2, -5, 10))

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(4))




# print(isinstance(test, object))