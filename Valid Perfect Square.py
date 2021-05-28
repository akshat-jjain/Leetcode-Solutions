class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s=str(num**.5)
        return not int(s[s.index('.')+1:])
