class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        b = []
        for x in nums:
            if b.count(x)<2:b.append(x)
        nums[:]=b
        return len(b)
