def even_odd(A: list[int]) -> None:
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1


# Test
listA = [32,21,43,55,66,37,62,22,33]

even_odd(listA)

print(listA)