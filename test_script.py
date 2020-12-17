from sympy.solvers.diophantine import cornacchia
from common import get_absolute_value
import timeit
from simplified_cornacchia import is_prime_by_ben_simplified_cornacchia

def is_prime_by_ben(N):
    sol = []
    for d in range(1, 3):
        sols = cornacchia(1, -D, N // d ** 2)
        if sols:
            for x, y in sols:
                sol.append((d * x, d * y))
                if D == -1:
                    sol.append((d * y, d * x))
    return len(sol) == 1

general_start = timeit.default_timer()
data_points = []
for k in range(20, 21):
    print("evaluating x1:" + str(k))
    x, y = 10 ** k + 1, 10 ** k + 13

    z = get_absolute_value(x, y)
    print("evaluating if following number is prime: " + str(z))
    D = -163
    N = 4 * z
    start = timeit.default_timer()
    if (is_prime_by_ben(N)):
        stop = timeit.default_timer()
        data_points.append((k, stop - start, x, y, z))
        print("PRIME DETECTED")
    else:
        stop = timeit.default_timer()
general_stop = timeit.default_timer()
print("Final result: ")
print("produced in: ")
print(stop - start)
final_result = (data_points)

print(data_points)
