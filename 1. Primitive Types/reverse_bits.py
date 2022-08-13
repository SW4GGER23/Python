from swap_bits import swap_bits

# Reverse 16-bit integer
def reverse_bits16(x: int) -> int:
    for i in range(0, 8):
        x = swap_bits(x, i, 15 - i)
    return x

# Reverse 64-bit integer
def reverse_bits64(x: int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    return (reverse_bits16((x >> (0 * mask_size)) & bit_mask) << (3 * mask_size) | 
            reverse_bits16((x >> (1 * mask_size)) & bit_mask) << (2 * mask_size) | 
            reverse_bits16((x >> (2 * mask_size)) & bit_mask) << (1 * mask_size) |
            reverse_bits16((x >> (3 * mask_size)) & bit_mask) << (0 * mask_size) )


# Test
n = 0b10010011
print(bin(reverse_bits64(n)))
