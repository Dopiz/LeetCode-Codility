def isMonotonic(self, A):
    """
    :type A: List[int]
    :rtype: bool
    """
    return A == sorted(A) or A[::-1] == sorted(A)