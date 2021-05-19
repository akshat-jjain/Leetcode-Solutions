class Solution:
    def isHappy(self, n: int) -> bool:
        a =[]
        flag=0
        s=0
        while 1 :
            s=0
            while n:
                a1=(n%10)**2
                s+=a1
                n=int(n/10)
            if s in a:
                break
            else:
                if s==1 :
                    flag=1
                    break
                a.append(s)
                n=s
        return flag
