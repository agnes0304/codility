# Assume that:
# 01: N and K are integers within the range [0..100]
# 02: each element of array A is an integer within the range [−1,000..1,000].
# In your solution, focus on correctness.

def cyclicRotation(A, K):
    if A:
        if K <= len(A):
            if K == 0 or K == len(A):
                return A
            else:
                return A[len(A)-K:] + A[:len(A)-K]
        else:
            if len(A) == 2 and K % 2 == 0:
                return A
            else:
                i = K % len(A)
                return A[len(A)-i:] + A[:len(A)-i]
    else:
        return A
