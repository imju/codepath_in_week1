class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        sorted_A = sorted(A)
        if len(A)%2 == 0:
            stop = len(A)
        else:
            stop = len(A)-1
        for i in range(0, stop,2):
            temp = sorted_A[i]
            sorted_A[i] = sorted_A[i+1]
            sorted_A[i+1]= temp
        return sorted_A
