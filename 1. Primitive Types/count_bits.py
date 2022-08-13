#Count the number of 1's in x
def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

#result = count_bits(9)
#print(result)
