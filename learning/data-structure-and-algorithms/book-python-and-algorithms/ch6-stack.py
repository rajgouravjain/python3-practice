class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return (self.stack == [])
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
def par_checker():

if __name__ == "__main__":
    # s1 = Stack()
    # s1.push("Hello")
    # s1.push("Bye")
    #
    # print(s1.peek())
    # print(s1.size())
    # print(s1.pop())
    # print(s1.pop())
    #
    # print(s1.isEmpty())