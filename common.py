import math

# Definition of constants!

C = 41


def get_absolute_value(c, d):
    """ Returns the value of the function c²+cd+d²*C """
    return c ** 2 + c * d + C * d ** 2


def f(x, y=1):
    """ Returns the value of the function x²+xy+y²*C """
    return get_absolute_value(x, y)


def is_prime(n):
    """ Checks if a number is prime by trial division """
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def is_prime_cd(c, d):
    """ Checks if a number of the form (c,d) is prime, using is_prime function """
    return is_prime(get_absolute_value(c, d))


def get_primes(n, m):
    """ Generates a list of all prime numbers between n and m. """
    # Initialize a list
    primes = []
    for possiblePrime in range(n, m):
        if is_prime(possiblePrime):
            primes.append(possiblePrime)
    return primes


def calcxy(x, y):
    return (C * (C * x ** 2 + 2 * x * y + x + 1) + (y ** 2 + y))


def calc_klmn(k, l, m, n):
    """
        Calculates the product of (x1,y1)*(x2,y2) = ((x1+y1*alpha)*(x2+y2*_alpha_)) * (x1+y1*_alpha_)*(x2+y2*alpha)).
        alpha = (1+(sqrt(1-4*C))/2. _alpha = (1-sqrt(1-4*C))/2
        lambda = C
        Result is splitted into three parts (result, C**2 part, C part, 1 part)
     """
    c2 = (l * n) ** 2
    c = l ** 2 * m * n + l ** 2 * m ** 2 + k * l * n ** 2 + k ** 2 * n ** 2
    z = (k ** 2 * m ** 2 + k ** 2 * m * n + k * l * m ** 2 + k * l * m * n)
    return C ** 2 * c2 + C * c + 1 * z, c2, c, z


def get_X_Y_values(x1, y1, x2, y2):
    """

    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return: X1, Y1, X2, Y2
    """

    X1 = -(x1 + y1) * (x2 + y2) + (y1 * y2 * C)
    Y1 = y1 * x2 + x1 * y2 + y1 * y2

    X2 = x1 * x2 + x1 * y2 + y1 * y2 * C
    Y2 = y1 * x2 - x1 * y2

    return X1, Y1, X2, Y2


def check_alternative(x1, y1, x2, y2):
    """
    :param x1: x1 value
    :param y1: y1 value
    :param x2: x2 value
    :param y2: y2 value
    :return: multiple results 1) Absolute value of (x1,y1)*(x2,y2) 2) x value of the end result 3) y value of the end result
    """
    if y1 * x2 > x1 * y2:
        c = x1 * x2 + C * y1 * y2 + x1 * y2
        d = (y1 * x2 - x1 * y2)
    else:
        c = x1 * x2 + C * y1 * y2 + x1 * y2
        d = (y1 * x2 - x1 * y2)
        print('did not do it, change x1y1 with x2y2')
    return get_absolute_value(c, d), c, d


def get_quadratic_residues(modulus=4 * C - 1):
    """ Generates a list of all quadratic residues a given a modulus (standard 4*C-1) """
    quadratic_residues = []
    for a in range(1, modulus + 1):
        for b in range(1, math.ceil((modulus - 1) / 2 + 1)):
            if (b ** 2) % modulus == a:
                quadratic_residues.append(a)

    return quadratic_residues


def get_quadratic_residues_simplified(modulus=4 * C - 1):
    """ Generates a list of all quadratic residues a = x^2 mod y2 with y2 = (standard 4*C-1) """
    quadratic_residues = []
    for b in range(1, math.ceil((modulus - 1) / 2 + 1)):
        quadratic_residues.append((b ** 2) % modulus)
    return sorted(quadratic_residues)


def find_quadratic_results(a, n):
    """ Returns a list of all the solutions x of x² = a mod y2"""
    solutions = []
    for x in range(1, n):
        if ((x ** 2) % n == a % n):
            solutions.append(x)
    return solutions


def remove_duplicate_values(list):
    """ Converts a list and removes all duplicate values"""
    # initialize a null list
    unique_list = []
    # traverse for all elements
    for x in list:
        # check if exists in unique_list or nots
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list


def calculate_discriminant(a, b, c):
    return (b * b) - (4 * a * c)


def calculate_roots(a, b, c):
    discriminant = (b * b) - (4 * a * c)
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant) / (2 * a))
        root2 = (-b - math.sqrt(discriminant) / (2 * a))
        return [root1, root2]
    elif discriminant == 0:
        root1 = root2 = -b / (2 * a)
        return [root1]
    elif discriminant < 0:
        root1 = root2 = -b / (2 * a)
        imaginary = math.sqrt(-discriminant) / (2 * a)
        return None


def is_square(number):
    x = number // 2
    seen = {x}
    while x * x != number:
        x = (x + (number // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


def is_perfect_square(x):
    if x > 0:
        # Find floating point value of
        # square root of x.
        sr = math.sqrt(x)

        # If square root is an integer
        return (sr - math.floor(sr)) == 0
    else:
        return False


def modular_quadratic_polynomial_solver(a, b, c, p):
    # Based on https://math.stackexchange.com/questions/551700/when-is-the-quadratic-congruence-ax2-bx-c-equiv-0-pmod-p-solvable
    return None
