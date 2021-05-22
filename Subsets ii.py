from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        a=[]
        for x in range(len(nums)+1):
            a+=set(list(itertools.combinations(sorted(nums), x)))
        a[:]=[list(x) for x in a ]
        return a
