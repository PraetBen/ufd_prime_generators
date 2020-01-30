from sympy.ntheory.primetest import isprime
from sympy.solvers.diophantine import diophantine, symbols, diop_solve, cornacchia

L = 41
c, d = 11, 13


def get_absolute_value(c, d):
    return (c ** 2 + c * d + L * d ** 2)


def is_prime_by_ben(c, d):
    L = 41
    x, y = symbols("x y", integer=True)
    z = get_absolute_value(c, d)
    sol = diop_solve(x ** 2 + x * y + L * y ** 2 - z)
    print(sol)
    return len(sol) == 4



print(is_prime_by_ben(c, d))

print(get_absolute_value(c, d))
