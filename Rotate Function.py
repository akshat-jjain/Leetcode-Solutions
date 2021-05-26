class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        a2=sum(x*y for x,y in enumerate(nums))
        maxSum=a2
        for x in range(1,len(nums)):
            a2+=sum(nums)-len(nums)*nums[-x]
            maxSum=max(a2,maxSum)
        return maxSum
