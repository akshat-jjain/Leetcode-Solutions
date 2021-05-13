class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in nums:
            rem = int(target-int(x))
            if rem in nums[nums.index(x)+1:]:
                return [nums.index(x),nums.index(rem,nums.index(x)+1)]
