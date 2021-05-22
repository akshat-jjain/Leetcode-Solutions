class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n1=set(nums)
        if len(n1) == len(nums):return []
        abc = set()
        for x in sorted(nums):
            if x in n1:n1.remove(x)
            elif x not in abc :abc.add(x)
        return abc
