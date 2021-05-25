from itertools import permutations as ip
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        b=list(ip([x for x in range(1,n+1)],n))
        
        return  ''.join([str(x) for x in b[k-1]] )
