class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s=="" and goal=="":return True
        for x in range(len(s)):
            s1=s[x+1:]+s[:x+1]
            if s1==goal:
                return True
        return False
