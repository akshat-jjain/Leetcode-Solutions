class Solution:
    def isNumber(self, s: str) -> bool:
        if 'inf'in s.lower() : return 0
        try:
            a=float(s)
            return 1
        except:
            return 0
