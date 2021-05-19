class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        flag=0
        if n<0:
            return 0
        for x in range(int(n**0.5)+2):
            if 2**x==n:
                flag=1
                break
         
        return flag
