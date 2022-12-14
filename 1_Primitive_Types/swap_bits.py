def swap_bits(x, i, j):
    # Extract the i-th and j-th bits, and see if they differ.
    if(x >> i) & 1 != (x >> j) & 1:
        # i-th and j-th bits differ. We will swap them by flipping their values.
        # Select the bits to flip woith bit_mask. Since x^1 = 0 when x = 1 and 1
        # when x = 0, we can perform the flip XOR.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


# Test
n = 4
print(swap_bits(n, 2, 0))
