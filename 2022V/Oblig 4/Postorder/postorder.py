""" !!! Skrevet i sammarbeid med Jørgen Nordås og Konrad Simsøn !!! """


# Hentet fra Pearson
class Stack:
    def __init__(self):
        self.__elements = []

    # Return true if the stack is empty
    def isEmpty(self):
        return len(self.__elements) == 0

    # Returns the element at the top of the stack
    # without removing it from the stack.
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.__elements) - 1]

    # Stores an element into the top of the stack
    def push(self, value):
        self.__elements.append(value)

    # Removes the element at the top of the stack and returns it
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop()

    # Return the size of the stack
    def __len__(self):
        return len(self.__elements)


# Data structure to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Iterative function to perform postorder traversal on the tree
def PostOrder(root):

    # return if the tree is empty
    if root is None:
        return

    # create an empty stack and push the root node
    stack = Stack()
    stack.push(root)

    # create another stack to store postorder traversal
    out = Stack()

    # loop till stack is empty
    while stack:

        # pop a node from the stack and push the data into the output stack
        curr = stack.pop()
        out.push(curr.data)

        # push the left and right child of the popped node into the stack
        if curr.left:
            stack.push(curr.left)

        if curr.right:
            stack.push(curr.right)

    # print postorder traversal
    while out:
        print(out.pop(), end=" ")


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    PostOrder(root)
