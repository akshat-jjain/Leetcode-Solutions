class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums.count(target): return nums.index(target)
        return -1
