import itertools as it
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(it.combinations([x for x in range(1,n+1)], k))
