class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        a=nums[0]
        b=nums[0]
        c=[]
        for x in nums[1:]:
            if b+1==x:b=x
            else:
                if a==b:
                    c.append(str(a))         
                else:
                    c.append("{}->{}".format(a,b))
                a=x
                b=x

        if a==b:
            c.append(str(a))
                             
        else:
            c.append("{}->{}".format(a,b))

        return c
