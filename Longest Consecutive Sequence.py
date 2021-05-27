class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : return (0)
        nums[:]=list((sorted(nums)))
        c=1
        a=0
        for x in range(len(nums)-1):
            if nums[x+1]-nums[x]==1 or  nums[x]== nums[x+1] :

                if nums[x]== nums[x+1]:
                    continue
                c+=1
                continue

            if c>a:
                a=c
            c=1
        return (c if c>a else a)
