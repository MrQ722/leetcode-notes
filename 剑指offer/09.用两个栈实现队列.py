class CQueue:

    def __init__(self):
        self.tmp = []

    def appendTail(self, value: int) -> None:
        self.tmp.append(value)

    def deleteHead(self) -> int:
        if len(self.tmp) == 0:
            return -1
        else:
            return self.tmp.pop(0)

# 使用两个栈
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack2:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop() if self.stack2 else -1
        else:
            return self.stack2.pop()
