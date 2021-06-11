class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        while n-i>=0:
            n-=i
            i+=1
        return (i-1)
