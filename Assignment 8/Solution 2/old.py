from testInput import testInput
import cProfile


class Node:
    def __init__(self, importance):
        self.importance = importance
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.max = 0

    def push(self, importance):
        newN = Node(importance)
        newN.next = self.head
        self.head = newN
        if importance > self.max:
            self.max = importance

    def pop(self):
        popped = self.head.importance
        self.head = self.head.next
        if popped == self.max:
            self.findMax()
        return popped

    def findMax(self):
        current = self.head
        self.max = 0
        while current:
            if current.importance > self.max:
                self.max = current.importance
            current = current.next


def main():
    inps = 814
    actions = []
    stack = Stack()
    tmp = testInput()
    inputs = tmp.split("\n")
    for x in range(inps):
        a = inputs[x]
        if a == "2":
            stack.pop()
        elif a == "3":
            print(stack.max)
        else:
            prior = int(a.split(" ")[1])
            stack.push(prior)


cProfile.run('main()')
