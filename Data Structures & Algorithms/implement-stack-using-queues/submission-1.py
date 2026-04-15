class MyStack:

    def __init__(self):
        self.que = []
        self.leng = 0

    def push(self, x: int) -> None:
        self.que.append(x)
        self.leng += 1
        i = self.leng

        while i > 1:
            self.que.append(self.que.pop(0))
            i -= 1

    def pop(self) -> int:
        self.leng -= 1
        return self.que.pop(0)


    def top(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        if self.que:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()