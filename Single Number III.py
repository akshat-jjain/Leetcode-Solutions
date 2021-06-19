class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        b=[]
        a=list(set(nums))
        for x in a:
            if nums.count(x)==1: b.append(x)
        return b
