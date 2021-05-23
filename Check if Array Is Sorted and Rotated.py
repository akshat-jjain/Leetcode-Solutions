class Solution:
    def check(self, nums: List[int]) -> bool:
        if sorted(nums) == nums:return (True)
        for x in range(1, len(nums)):
            if sorted(nums) == nums[-x:]+nums[:len(nums)-x]:return (True)
        return False
