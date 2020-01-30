from sympy import *
from common import is_prime

x = Symbol('x')
a, b, c = 1, 1, 7
startPoint = -1
f = a * x ** 2 + b * x + c

cutoff = 100

def main():
    composites = find_composites(cutoff)
    print('Detected composites:')
    composites.sort()
    print(composites)
    mistakes = check_primes(composites, cutoff)
    print('mistakes:')
    mistakes.sort()
    print(mistakes)


def find_composite_functions(cutoff):
    composite_positions = []
    divider_1 = []
    divider_2 = []
    counter = 0

    # creation of first composite
    composite_positions.append(x + f.subs(x, x))
    divider_1.append(f.subs(x, x))
    divider_2.append(simplify(f.subs(x, x + f.subs(x, x)) / f.subs(x, x)))

    # run the algorithm as long as there are still composites to treat
    while counter < len(composite_positions):
        pos_composite1 = composite_positions[counter] + divider_1[counter]
        if pos_composite1.subs(x, startPoint) < cutoff:
            composite_positions.append(pos_composite1)
            divider_1.append(divider_1[counter])
            del2 = f.subs(x, pos_composite1) / divider_1[counter]
            divider_2.append(del2)

            pos_composite2 = composite_positions[counter] + divider_2[counter]
            if pos_composite2.subs(x, startPoint) < cutoff:
                composite_positions.append(pos_composite2)
                divider_1.append(divider_2[counter])
                # del2 = f.subs(x, pos_composite1) / err_del1[counter]
                divider_2.append(del2)  # gebruik makend dat er gemeenschappelijke deler is blijkbaar
        counter += 1
    return composite_positions


def find_composites(cutoff):
    composite_functions = find_composite_functions(cutoff)
    err_pos = []
    for function in composite_functions:
        print(simplify(function))
        h = startPoint
        while function.subs(x, h) < cutoff:
            err_pos.append(function.subs(x, h))
            h += 1
    return err_pos


def check_primes(composites, cutoff):
    mistakes = []
    for i in range(1, cutoff):
        if not i in composites:
            if not is_prime(f.subs(x, i)):
                mistakes.append(i)
                # print('failed at i' + str(i))
    return mistakes


if __name__ == '__main__':
    main()
