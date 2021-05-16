class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=[x for x in s if x.isalnum() ]
        return s==s[::-1]
