class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return 0
        return sorted(list(s))==sorted(list(t))
