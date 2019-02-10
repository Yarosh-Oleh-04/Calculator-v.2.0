"""
>>> node1 = Node('(')
>>> node2 = Node('1')
>>> node3 = Node(')')
>>> node3.next = node2
>>> node2.next = node1
>>> node3.data
')'
>>> node3.next.data
'1'
>>> node3.next.next.data
'('
>>> node3.next.next.next

>>>
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, topNode=None):
        self.topNode = topNode

    def top(self):
        return self.topNode.data

    def push(self, data):
        node = Node(data, self.topNode)
        self.topNode = node

    def pop(self):
        data = self.topNode.data
        self.topNode = self.topNode.next
        return data

    def isEmpty(self):
        return self.topNode is None


# stack = Stack()
# stack.push('(')
# stack.push('1')
# stack.push(')')
#
# print(stack.top())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.isEmpty())

if __name__ == "__main__":
    import doctest

    doctest.testmod()

