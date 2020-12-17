from sympy.ntheory.primetest import isprime
from sympy.solvers.diophantine import diophantine, symbols, diop_solve, cornacchia, sqrt_mod
from common import get_absolute_value

L = 41
k = 3
c, d = 61,7


def is_prime_using_diop_solve(c, d):
    print('Evaluating (' + str(c) + ', ' + str(d) + ') = ' + str(get_absolute_value(c, d)))
    x, y = symbols("x y", integer=True)
    z = get_absolute_value(c, d)
    sol = diop_solve(x ** 2 + x * y + L * y ** 2 - z)
    print('Found following (c, d) pairs that are equal to same absolute value: ')
    print(sol)
    return len(sol) == 4

def is_prime_using_diop_solve_single_number(z):
    print('Evaluating (' + str(c) + ', ' + str(d) + ') = ' + str(z))
    x, y = symbols("x y", integer=True)
    sol = diop_solve(x ** 2 + x * y + L * y ** 2 - z)
    print('Found following (c, d) pairs that are equal to same absolute value: ')
    print(sol)
    return len(sol) == 4

def solve_simplified_equation_by_pell(c, d):
    x, y = symbols("x y", integer=True)
    z = get_absolute_value(c, d)
    sol = diop_solve(x ** 2 + 163*y**2 - 4*z)
    print('Found following solution pairs are found: ')
    print(sol)
    return len(sol) == 4


#print(is_prime_using_diop_solve(1000001, 1000013))
#print(solve_simplified_equation_by_pell(1111321, 12313131))
#is_prime_using_diop_solve_single_number(263810319061)
v = sqrt_mod(163, 1720000000000000000432800000000000000027772, all_roots=False)
print(v)

