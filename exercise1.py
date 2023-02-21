import math


def f(x):
    return math.cos(x) + x


def g(x):
    return 1 - math.sin(x)


x = -1
for i in range(10):
    x = x - (f(x) / g(x))
    print(x)

# -------- better way of calculating---------
# you can uncomment below and comment the top to see

# x = -1
# y = 2
# while float('%.4f' % x) - float('%.4f' % y) != 0:
#     t = x
#     x = x - (f(x) / g(x))
#     y = t
#     print(x)

