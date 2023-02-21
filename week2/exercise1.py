import math


def f(x):
    return math.sin(3 * x)


def g(x):
    return 3 * math.cos(3 * x)


def forward_diff(x, h):
    return (f(x + h) - f(x)) / h


def central_diff(x, h):
    return (f(x - h) + f(x + h)) / (2 * h)


x = 2
h = 1
first = True
for i in range(5):
    forward = forward_diff(x, h)
    central = central_diff(x, h)
    real = g(x)
    print('h = ', h)
    print('estimated forward value : ', forward)
    print('forward error : ', abs(real - forward))
    print('estimated central value : ', forward)
    print('central error : ', abs(real - central))
    print()
    h = h / 2



