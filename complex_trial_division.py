from common import get_absolute_value


def find_complex_composites(c_input, d_input):
    test_value = get_absolute_value(c_input, d_input)
    composites = []
    c = 0
    d = 1

    composite_c_pos = get_absolute_value(c, d)
    composite_c_neg = get_absolute_value(-c, d)
    while composite_c_pos < test_value:
        while composite_c_pos < test_value:
            if test_value % composite_c_pos == 0:
                print(str(composite_c_pos) + ' divides ' + str(test_value))
                print('c = ' + str(c) + ' d = ' + str(d))
                composites.append([c, d])
            if test_value % composite_c_neg == 0:
                print(str(composite_c_neg) + ' divides ' + str(test_value))
                print('c = -' + str(c) + ' d = ' + str(d))
                composites.append([-c, d])
            c += 1
            composite_c_pos = get_absolute_value(c, d)
            composite_c_neg = get_absolute_value(-c, d)
            # print('c = ' + str(c) + ' d = ' + str(d))
        d += 1
        c = 0
        composite_c_pos = get_absolute_value(c, d)
        composite_c_neg = get_absolute_value(-c, d)
    return composites


def is_prime_complex_trial_division(c_input, d_input):
    print('Evaluating (' + str(c_input) + ', ' + str(d_input) + ') = ' + str(get_absolute_value(c_input, d_input)))

    # be careful, sometimes d=0 is a valid case! for example c,d = 9,12
    # TODO: check if the abs_val is a quadratic? or simple algorithm looping all over c values while d=0

    return len(find_complex_composites(c_input, d_input)) == 0


print(is_prime_complex_trial_division(5, 0))
