class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0: return 0
        p=1
        while n!=1:
            p*=n
            n-=1
        s1=str(p)[::-1]
        
        return (len(s1)-len(str(int(s1))))
