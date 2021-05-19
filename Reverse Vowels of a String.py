class Solution:
    def reverseVowels(self, s: str) -> str:
        b=''
        s1=''
        for x in s:
            if x.lower() in ['a','e','i','o','u','A','E','I','O','U']:
                b+=x
        b=b[::-1]
        i=0
        for x in range(len(s)):
            if s[x] in ['a','e','i','o','u','A','E','I','O','U']:
                s1+=b[i]
                i+=1
            else: 
                s1+=s[x]    
        return s1
