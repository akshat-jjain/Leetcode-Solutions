class Solution:
    def reverse(self, x: int) -> int:
        if x >= (2**31)-1 or x <= -2**31:return 0
        else :
            x=str(x)
            if x=="0":return 0
            if x>"0":
                x=x.strip('0')[::-1]
            else:    
                x=x[1::]
                x="-"+x.strip('0')[::-1]
            if int(x) >= (2**31)-1 or int(x) <= -2**31:return 0
            else:return x
