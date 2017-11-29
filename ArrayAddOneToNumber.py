class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 0
        result = []
        is_leading_zero = True
        leading_zero_index = -1
        trimmed = []
        if len(A)==1 and A[0]==0:
            trimmed = A
        else:
            for i in range(len(A)):
                if is_leading_zero:
                    if A[i]==0:
                        continue
                    else:
                        is_leading_zero = False
                        trimmed.append(A[i])
                else:
                    trimmed.append(A[i])


        for i in range(len(trimmed)-1,-1,-1):
            if i == len(trimmed) -1:
                a= trimmed[i]+1
            else:
                a = trimmed[i]+carry
            #print(a)
            if a>9:
                trimmed[i] = a%10
                carry = int(a/10)
            else:
                trimmed[i] = a
                carry = 0
        if carry > 0 :
            trimmed.insert(0,carry)
        return trimmed  
