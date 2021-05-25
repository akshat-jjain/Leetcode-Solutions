from itertools import permutations as ip
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(list(ip(nums,len(nums))))
