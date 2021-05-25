class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=0
        b=list(magazine)
        for x in ransomNote:
            if x in magazine:
                try:
                    b.remove(x)
                    c+=1
                except:
                    break
        return c==len(ransomNote)
            
        return False
