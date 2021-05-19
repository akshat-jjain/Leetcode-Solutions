class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=sorted(nums, key=nums.count, reverse=False)
        return a[0]
