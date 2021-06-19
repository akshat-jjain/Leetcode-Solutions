class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=list(set(nums))
        b=[]
        for x in a: 
            if nums.count(x)>len(nums)//3: b.append(x)
        return b
