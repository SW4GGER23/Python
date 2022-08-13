def multiply(num1: list[int], num2: list[int]) -> list[int]:
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[i]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove the leading zeroes.
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]

    return [sign * result[0]] + result[1:]


# Test
res = multiply([1,0], [1,1])
print(res)