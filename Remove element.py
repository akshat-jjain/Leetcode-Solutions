class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for x in range(nums.count(val)):
            if x!=val:
                nums.remove(nums[nums.index(x)])
        return len(nums)
