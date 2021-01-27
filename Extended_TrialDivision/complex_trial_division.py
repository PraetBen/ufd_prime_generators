# %%
from common import get_absolute_value
from sympy import isprime


def is_prime_trial_division_in_ufd(x, y):
    """ Checks if (x, y) is prime by trial division in the UFD (defined in get_absolute_value) """
    x_y_value = get_absolute_value(x, y)
    x1, y1 = 2, 0  # start point is (2,0) as (0,0) equals 0 and (1, 0) equals 1
    x1_y1_value = get_absolute_value(x1, y1)
    x1_neg_y1_value = get_absolute_value(-x1, y1)
    while x1_y1_value <= int(x_y_value ** 0.5) or x1_neg_y1_value <= int(x_y_value ** 0.5):  # y-level loop
        while x1_y1_value <= int(x_y_value ** 0.5) or x1_neg_y1_value <= int(x_y_value ** 0.5):  # x-level loop
            if x_y_value % x1_y1_value == 0 or x_y_value % x1_neg_y1_value == 0:
                return False
            x1 += 1  # check next x1 value
            x1_y1_value = get_absolute_value(x1, y1)
            x1_neg_y1_value = get_absolute_value(-x1, y1)

        y1 += 1  # move to next y1 value to check
        x1 = 0  # reset x1 back to 0
        x1_y1_value = get_absolute_value(x1, y1)
        x1_neg_y1_value = get_absolute_value(-x1, y1)
    return True


def find_complex_composites(x, y):
    x_y_value = get_absolute_value(x, y)
    x1, y1 = 2, 0  # start point is (2,0) as (0,0) equals 0 and (1, 0) equals 1

    x1_y1_value = get_absolute_value(x1, y1)
    x1_neg_y1_value = get_absolute_value(-x1, y1)
    composites = []
    while x1_y1_value <= int(x_y_value) or x1_neg_y1_value <= int(x_y_value):  # y-level loop
        while x1_y1_value <= int(x_y_value) or x1_neg_y1_value <= int(x_y_value):  # x-level loop
            if x_y_value % x1_y1_value == 0:
                composites.append([x1, y1])
            if x_y_value % x1_neg_y1_value == 0:
                composites.append([-x1, y1])
            x1 += 1
            x1_y1_value = get_absolute_value(x1, y1)
            x1_neg_y1_value = get_absolute_value(-x1, y1)
        # move to next y value to check
        x1 = 0
        y1 += 1
        x1_y1_value = get_absolute_value(x1, y1)
        x1_neg_y1_value = get_absolute_value(-x1, y1)
    return composites


def is_prime(N):
    """ Checks if a number is prime by simple trial division """
    x = 2  # initialize variable
    while x <= int(N ** 0.5):  # while x is smaller than the square root of N
        if N % x == 0:  # if N is divisible by x
            return False  # then N is not a prime
        x += 1  # add one more to x to test the next number
    return True  # when no x can be found that divides N, then N must be a prime number

def check_algorithm(final_x, final_y):
    # check to see if the algorithm is working
    for c in range(0, final_x):
        for d in range(1, final_y):
            if isprime(get_absolute_value(c, d)) != is_prime_trial_division_in_ufd(c, d):
                print(c, d)
        print("evaluating: " + str(c))

    return True

