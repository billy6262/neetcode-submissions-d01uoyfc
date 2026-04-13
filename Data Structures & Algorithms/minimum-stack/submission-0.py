class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []

    def push(self, val: int) -> None:
        if len(self.mstack) == 0 or val < self.mstack[-1]:
            self.mstack.append(val)
        else:    
            self.mstack.append(self.mstack[-1])
        self.stack.append(val)
        
    def pop(self) -> None:
        self.mstack.pop()
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]
