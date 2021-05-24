class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend>0 and divisor<0 or dividend<0 and divisor>0:ans= -1*(abs(dividend)//abs(divisor))
        else:ans=(abs(dividend)//abs(divisor))
        if -2**31 <= ans <= 2**31 - 1:return ans
        elif ans>2**31-1:return 2**31-1
        else:return -2**31
