class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp=[]
        for x in matrix:
            temp+=x
        temp.sort()
        return temp[k-1]
