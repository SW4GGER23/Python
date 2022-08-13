#
# Takes as input a nonnegative integer x and returns a number y which is
# not equal to x, but has the same weight as x and their difference, |y-x|,
# is as small as possible.
#
# Define the weight of a nonnegative integer x to be the number of bits that
# are set to 1 in its binary representation.
#
# Time complexity: O(n)
def closest_int_same_weight(x: int) -> int:
    num_unsigned_bits = 64
    for i in range(num_unsigned_bits - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1))
            return x

    # Raise error if all bits of x are 0 or 1.
    raise ValueError("All bits are 0 or 1")

# Time and space complexity: O(1)
def closest_int_same_weight2(x: int) -> int:
    ls1bit = x & ~(x - 1) # Only least significant 1 bit is set to 1; Ex. 11011 -> 00001
    ls0bit = ~x & (x + 1) # Only least significant 0 bit is set to 1; Ex. 11011 -> 00100

    if ls1bit == 0:
        raise ValueError("All bits are 0")
    elif ls0bit == 0:
        raise ValueError("All bits are 1")

    if ls1bit > ls0bit:
        swap_mask = ls1bit | (ls1bit >> 1)
    else:
        swap_mask = ls0bit | (ls0bit >> 1)
    
    x ^= swap_mask
    return x


# Test
n = 34
print(closest_int_same_weight(n))
print(closest_int_same_weight2(n))
