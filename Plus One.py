class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b=0
        for x in range(len(digits)):
            b+= digits[x]*(10**(len(digits)-x-1))
        b+=1
        return [int(x) for x in str(b)]
