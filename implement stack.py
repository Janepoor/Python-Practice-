
class Stack:

    def __init__(self,size):
        self.size = size
        self.stack = []

    def __str__(self):

        return str(self.stack)

    def getSize(self):
        return len(self.stack)


    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def isFull(self):
        if(len(self.stack)) == self.size:
            return True
        else:
            return False


    def push(self,x):
        if self.isFull():
            raise Exception("Stack is full")
        else:
            self.stack.append(x)

    def pop(self):
        if self.isEmpty():
            return -1

        top = self.stack[-1]
        self.stack.remove(top)
        return top



if __name__ == '__main__':
    stackTest = Stack(10)
    for i in range(10):
        stackTest.push(i)

    print(stackTest.getSize())
    print(stackTest.isEmpty())
    print(stackTest.isFull())
    print(stackTest)