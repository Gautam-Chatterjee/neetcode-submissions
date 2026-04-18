class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        currMin = self.getMin()
        if currMin == None or currMin > val:
            currMin= val
        self.stack.append((val,currMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1][1]
        else:
            return None
