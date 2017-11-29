class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        prefix = []
        i = 0
        prefix_continue = True

        while prefix_continue:
            if i < len(A[0]):
                temp = A[0][i]
            else:
                prefix_continue = False
                break
            #print(i)
            for a in A:
                #print('length:'+str(len(a)))
                if i == len(a):
                    prefix_continue = False
                    break
                if temp == a[i]:
                    continue
                else:
                    prefix_continue = False
                    break

            if prefix_continue:
                prefix.append(temp)
                i+=1
        return ''.join(prefix)
