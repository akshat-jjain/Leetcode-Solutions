class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums)==1 or k==0 :return nums
        elif k>len(nums):k%=len(nums)
        nums[:]=nums[-k:]+nums[:len(nums)-k]
        return nums
