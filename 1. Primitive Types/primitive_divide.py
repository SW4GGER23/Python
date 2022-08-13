# Time complexity: O(n)
def divide(x: int, y: int) -> int:
    result, power = 0, 32 # Suppose x >= (y * 2^32). 
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
        
        result += 1 << power
        x -= y_power
    return result

def divide2(x: int, y: int) -> int:
    isNeg = False

    if x < 0:
        x = 0 - x
        isNeg = ~isNeg
    if y < 0:
        y = 0 - y
        isNeg = ~isNeg

    result = divide(x, y)
    return result if isNeg == False else -result


# Test
n1 = divide(4214, 37)
n2 = divide2(361, -19)
print(n1)
print(n2)
