from sympy import sqrt_mod, gcdex
from common import get_absolute_value

D = -163

def igcdex(a, b):
    """Returns x, y, g such that g = x*a + y*b = gcd(a, b).

       >>> from sympy.core.numbers import igcdex
       >>> igcdex(2, 3)
       (-1, 1, 1)
       >>> igcdex(10, 12)
       (-1, 1, 2)

       >>> x, y, g = igcdex(100, 2004)
       >>> x, y, g
       (-20, 1, 4)
       >>> x*100 + y*2004
       4

    """
    if (not a) and (not b):
        return (0, 1, 0)

    if not a:
        return (0, b//abs(b), abs(b))
    if not b:
        return (a//abs(a), 0, abs(a))

    if a < 0:
        a, x_sign = -a, -1
    else:
        x_sign = 1

    if b < 0:
        b, y_sign = -b, -1
    else:
        y_sign = 1

    x, y, r, s = 1, 0, 0, 1

    while b:
        (c, q) = (a % b, a // b)
        (a, b, r, s, x, y) = (b, c, x - q*r, y - q*s, r, s)

    return (x*x_sign, y*y_sign, a)


def simplified_cornacchia(a, b, m):
    sols = 0

    a1 = 1
    v = sqrt_mod(-b * a1, m, all_roots=True)
    if not v:
        return None

    for t in v:
        if t < m // 2:
            continue

        u, r = t, m

        while True:
            u, r = r, u % r
            if a * r ** 2 < m:
                break

        m1 = m - a * r ** 2

        if m1 % b == 0:
            m1 = m1 // b
            sols += 1

    return sols

def is_prime_by_ben_simplified_cornacchia(N):
    sol = 0
    for d in range(1, 3):
        sols = simplified_cornacchia(1, -D, N // d ** 2)
        if sols:
            sol += sols
    return sol == 1

# %%

print(is_prime_by_ben(get_absolute_value(11, 12)))
