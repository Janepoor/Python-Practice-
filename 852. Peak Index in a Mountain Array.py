def peakIndexInMountainArray( A):
    """
    :type A: List[int]
    :rtype: int
    """
    low = 0
    high = len(A) - 1
    peak = 0

    while low <= high:
        mid = low + (high - low) / 2
        if A[mid - 1] < A[mid] > A[mid + 1]:
            peak = mid
            break
        elif A[mid - 1] < A[mid] < A[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

    return peak