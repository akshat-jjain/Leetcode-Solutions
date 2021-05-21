class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        i=[]
        for x in range(len(matrix)):
            if 0 in matrix[x]:
                if matrix[x].count(0)>1:
                    for y in range(len(matrix[x])):
                        if matrix[x][y]==0:
                            i.append(y)
                else:i.append(matrix[x].index(0))
                matrix[x][:]=[0 for y in matrix[x]]
        for x in i:
            for y in range(len(matrix)):
                matrix[y][x]=0
