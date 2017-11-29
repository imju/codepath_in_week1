class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        result = 0
        i = len(A)-1
        while i >= 0 :
            #print(A[i]+' result:'+str(result))
            if A[i]=='I':
                result += 1
                i-=1
                continue
            elif A[i]=='V':
                result += 5
                i-=1
                if i>=0 and A[i]=='I':
                    result -= 1
                    i-=1
                #print('result:'+str(result)+' A[i]:'+A[i])
                continue
            elif A[i]=='X':
                result += 10
                i-=1
                if i>=0 and A[i]=='I':
                    result -= 1
                    i-=1
                continue
            elif A[i]=='L':
                result += 50
                i-=1
                if i>=0 and A[i]=='X':
                    result -= 10
                    i-=1
                continue
            elif A[i]=='C':
                result += 100
                i-=1
                if i>=0 and A[i]=='X':
                    result-=10
                    i-=1
                continue
            elif A[i]=='D':
                result += 500
                i-=1
                if i>=0 and A[i]=='C':
                    result -= 100
                    i-=1
                continue
            elif A[i]=='M':
                result +=1000
                i-=1
                if i>=0 and A[i]=='C':
                    result -= 100
                    i-=1
                continue
        #print('result:'+str(result))
        return result
