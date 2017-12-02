print("Hello")
'''
input1:
{1, 2, 2}
stars
{1, 2, 1} : total: 4

'''

class Solution:

  #@param A a list of ranking
  #return total number of stars
  def goldStarList(A):
    stars = []


    for i in range(len(A)):
      stars.append(1) #initialization
      left=0
      if i == 0 :
        left = A[-1]
      elif i > 0 :
        left = A[i-1]

      if A[i] > left:
        stars[i] += 1

    total = 0
    for s in stars:
      total += s
    return total  
