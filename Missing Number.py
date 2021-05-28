class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(nums[-1]):
            if x not in nums:
                return x
        return nums[-1]+1
