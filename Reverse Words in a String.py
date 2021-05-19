class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        a.reverse()
        b=' '.join(a)
        return b
