class MinStack:
    def _init_(self):
        self.a=[]
        

    def push(self, val: int) -> None:
        (self.a).append(val)

    def pop(self) -> None:
        (self.a).pop()

    def top(self) -> int:
        return (self.a)[len(self.a)-1]

    def getMin(self) -> int:
        return min(self.a)
