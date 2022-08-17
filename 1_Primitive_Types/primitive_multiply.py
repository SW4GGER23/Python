# Time complexity: O(n^2); O(n) for addition, O(n) for iteration where n is 
# the number of the bits needed to represent the operands.
def multiply(x: int, y: int) -> int:
    def add(a, b):
        return a if b == 0 else add(a ^ b, (a & b) << 1) # (a & b) << 1 means carry of the sum.

    running_sum = 0
    while x: # Examines each bit of x.
        if x & 1:    
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum


# Test
n = multiply(19, 37)
print(n)
