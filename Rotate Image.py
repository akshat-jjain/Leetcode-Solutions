class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i=0
        j=0
        n=len(matrix)
        a1=[[0 for x in range(n)] for x in range(n)]
        for x in range(n):
            i=-x
            j=(n-1)-x
            for y in range(n):
                a1[x+i][y+j]=matrix[x][y]
                i+=1
                j-=1
        matrix[:]=a1
