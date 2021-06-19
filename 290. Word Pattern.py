class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p1,s1,flag,used=list(set(pattern)),s.split(),1,[]
        if len(list(pattern))!=len(s1): return 0
        for x in p1:
            word,temp1=s1[pattern.index(x)],pattern.index(x)
            if word in used: flag=0; break;
            for y in range(pattern.count(x)-1):
                temp1=pattern.index(x,temp1+1)
                if s1[temp1]!=word: 
                    flag=0
                    break
                if not flag: break
            used.append(word)
        if flag: return 1
        return 0
