import math


def f(x):
    return math.sin(x)


def g(x):
    return math.exp(-(math.sqrt(x)))


def trapezoidal(a, b, n, function):
    h = (b - a) / n
    if function == f:
        integration = f(a) + f(b)
        for i in range(1, n):
            k = a + i * h
            integration = integration + 2.0 * f(k)
    if function == g:
        integration = g(a) + g(b)
        for i in range(1, n):
            k = a + i * h
            integration = integration + 2.0 * g(k)
    return integration * h / 2


print(trapezoidal(1, 2, 100, f))
print(trapezoidal(0, 1, 100, g))
