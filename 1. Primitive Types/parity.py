#Brute-force method of checking parity 
#Time complexity is O(n) where n is the word size
def parity(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

#First improvement of checking parity
#Time complexity is O(k) where k is the number of bits set to 1 in a particular word
def parity1(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

#Second improvement of checking parity
#Time complexity is O(n/L) where L is the width of the words for which we cache the results and n is the word size
def parity2(x: int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    return (parity1(x >> (3 * mask_size)) ^ 
           parity1((x >> (2 * mask_size)) & bit_mask) ^ 
           parity1((x >> mask_size) & bit_mask) ^ 
           parity1(x  & bit_mask))

#Third improvement of checking parity
#Time complexity is O(log n) where n is the word size
def parity3(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1
