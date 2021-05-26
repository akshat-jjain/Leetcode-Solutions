class Solution:
    def addDigits(self, num: int) -> int:
        a=0
        while True:
            while num:
                a+=num%10
                num=int(num/10)
            if a>9: 
                num=a
                a=0
            else:
                break
        return a
