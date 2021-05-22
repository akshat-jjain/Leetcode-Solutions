from itertools import combinations as ic
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[]
        for x in range(len(nums)+1):
            a+=list(itertools.combinations(nums, x))
        a[:]=[list(x) for x in a]
        return a
