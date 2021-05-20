class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=int(len(nums)/2)
        b=list(set(nums))
        for x in b:
            if nums.count(x)>a:
                return x
