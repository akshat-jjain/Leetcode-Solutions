class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return sum([1 for x in matrix if target in x ])
