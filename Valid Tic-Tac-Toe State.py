class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def winner(x):
            if condition(0,0,0,1,0,2,x) or condition(1,0,1,1,1,2,x) or condition(2,0,2,1,2,2,x) or condition(0,0,1,0,2,0,x) or condition(0,1,1,1,2,1,x) or condition(0,2,1,2,2,2,x) or condition(0,0,1,1,2,2,x) or condition(0,2,1,1,2,0,x): return True
            return False
        def condition(a,b,c,d,e,f,val):
            if board[a][b] == board[c][d] == board[e][f] == val:return True
            return False
        def counting(val):return sum([board[x].count(val) for x in range(len(board))])
        if counting('O')==1 and counting('X')==0:return False
        if winner('X') and winner('O'):return False
        if (winner('X') and counting('X')<=counting('O')) or (winner('O') and counting('O')<counting('X')):return False
        if counting('X')-counting('O')>1:return False
        if counting('O')>counting('X'): return False
        if counting('X')+counting('O')==9:return True
        return True
