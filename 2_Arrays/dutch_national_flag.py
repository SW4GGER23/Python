RED, WHITE, BLUE = range(3)


def dutch_flag_partition1(pivot_index: int, A: list[int]) -> None:
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot.
    for i in range(len(A)):
        # Look for a smaller element.
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    # Second pass: group elements larger than pivot.
    for i in reversed(range(len(A))):
        # Look for a larget element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


def dutch_flag_partition2(pivot_index: int, A: list[int]) -> None:
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot.
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # Second pass: group elements larger than pivot.
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


def dutch_flag_partition(pivot_index: int, A: list[int]) -> None:
    pivot = A[pivot_index]
    # Keep the following invarinatns during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element.
    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot.
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal] 

# Test
A = [0, 1, 2, 0, 2, 1, 1]
dutch_flag_partition1(3, A)
print(A)

A = [0, 1, 2, 0, 2, 1, 1]
dutch_flag_partition2(3, A)
print(A)

A = [0, 1, 2, 0, 2, 1, 1]
dutch_flag_partition(1, A)
print(A)