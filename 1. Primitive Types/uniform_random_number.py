import random

def uniform_random(lower_bound: int, upper_bound: int) -> int:
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            # random.randrange(0, 2) returns 0 or 1 with equal probability.
            result = (result << 1) | random.randrange(0, 2)
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound


# Test
a, b, c = 0, 0, 0

for i in range(1000):
    ret = uniform_random(1, 3)

    if ret == 1:
        a += 1
    elif ret == 2:
        b += 1
    else:
        c += 1

print("%d %d %d" % (a, b, c))
