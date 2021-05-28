class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0: return False
        a=[2,3,5]
        i=0
        while n!=1:
            if n%a[i]==0:
                n=int(n/a[i])

                continue
            i+=1
            if i>2:
                return False

        return True
