class Solution:
    def isValid(self, s: str) -> bool:
        if s.count('(') == s.count(')') and s.count('[') == s.count(']') and s.count('{') == s.count('}'):
            dic = {'}':'{',']':'[',')':'('}
            a=[]
            for x in s:
                if x in [']',')','}'] and len(a)!=0 :
                    if a[-1] == dic[x] :a.pop()
                elif x in ['[','(','{']:a.append(x)
                else:return False
            if a:return False
            else:return True
        else:
            return False 
