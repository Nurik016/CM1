from math import *
from methods import bs


def f(x):
    return exp(x) - x**2


# Initial interval
a = -2
b = 0

print("========================")

root_bisection, iterations_bisection = bs.bisection_method(f, a, b)
if root_bisection is not None:
    print("Bisection method: Root:", root_bisection)
    print("Function value at the root:", f(root_bisection))
else:
    print("Bisection method: Did not converge or invalid interval")

print("========================")