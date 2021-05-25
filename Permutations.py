from itertools import permutations as ip
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(ip(nums,len(nums)))
