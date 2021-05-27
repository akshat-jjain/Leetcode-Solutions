class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def Arrange(x1, flag=0):
            if flag:
                return ['.' for x in range(x1.count('.')) ]+['#' for x in range(x1.count('#'))]+['*']
            return ['.' for x in range(x1.count('.')) ]+['#' for x in range(x1.count('#'))]
        for x in box:
            a=x.count('*')
            x1=[]
            while a:
                x1+=Arrange(x[:x.index('*')+1], 1)
                x[:]=x[x.index('*')+1:]
                a-=1
            x[:]=x1+Arrange(x)
        return [[box[x][y] for x in reversed(range(len(box)))] for y in range(len(box[0]))]
