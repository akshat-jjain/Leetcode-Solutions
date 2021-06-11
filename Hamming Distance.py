class Solution:
    def hammingDistance(self, x: int, y: int) -> int:            
        a=bin(x)[bin(x).index('b')+1:]
        b=bin(y)[bin(y).index('b')+1:]
        a='0'*(max(len(a), len(b))-len(a))+a
        b='0'*(max(len(a), len(b))-len(b))+b
        return (sum([1 for x in range(len(a)) if a[x]!=b[x]]))
