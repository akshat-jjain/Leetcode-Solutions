class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        b=[]
        if len(tokens)==1: return tokens[0]
        a1=0
        for x in tokens:
            if not x in ['+','-','*','/']:
                b.append(x)
                continue

            a1=str(int(eval(b[-2]+x+b[-1])))
            b.pop()
            b.pop()
            b.append(a1)
        return a1
