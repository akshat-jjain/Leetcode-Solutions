class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='': return '' 
        tel=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        s1=list(tel[int(digits[0])])
        for x in digits[1:]:
            s1=[x+y for y in tel[int(x)] for x in s1]
        return s1
