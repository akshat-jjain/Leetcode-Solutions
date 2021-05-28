class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for x in t:
            if s.count(x) < t.count(x):
                return x
