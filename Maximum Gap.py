class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        a=0
        b=nums[0]
        for x in range(1,len(nums)):
            if nums[x]-b>a:
                a=nums[x]-b
            b=nums[x]
                
        return a
