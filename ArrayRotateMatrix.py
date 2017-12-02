class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    #[
    #  [1, 2, 3]
    #  [4, 5, 6]
    #  [7, 8, 9]
    #]
    def rotate(self, A):
        n = len(A)
        if n == 1:
            return A
        mid = n/2
        if mid%2==0:
            mid = int(mid)
        else:
            mid = int(math.floor(mid))

        #transform (i,j) -> (j, i)
        for i in range(0, len(A)):
            #working on row i
            for j in range(0, i+1):
                #working on j in row i
                temp = A[i][j]
                A[i][j]= A[j][i]
                A[j][i]= temp
        #print(A)
        #transform (i,j) -> (i,symmetry of j)
        for i in range(0, len(A)):
            for j in range(0, mid):
                d = mid-j
                new_j = 0
                if n%2==0:
                    if d > 0:
                        new_j = j + 2*d - 1
                    elif d < 0:
                        new_j = j + 2*d + 1
                else:
                    new_j = j + 2*d
                #print('i:'+str(i)+' j:'+str(j)+':A: '+str(A[i][j])+ ' => i:'+str(i)+' j:'+str(new_j) +' :A: '+str(A[i][new_j]))
                temp = A[i][j]
                A[i][j] = A[i][new_j]
                A[i][new_j] = temp

        return A
