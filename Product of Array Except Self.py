class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zc=0
        prd=1
        for x in nums:
            if x==0:zc+=1
            else:prd*=x
        if zc==1:return [prd if x==0 else 0 for x in nums  ]
        if zc>1:return [0]*len(nums)
        else:return [prd//x for x in nums]
