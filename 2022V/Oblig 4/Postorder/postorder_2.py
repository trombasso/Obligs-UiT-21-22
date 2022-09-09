# Made in collaboration with Anders Karkskås and Jørgen Nordås


class Stack:
    def __init__(self):
        self.__elements = []

    # Return true if the stack is empty
    def is_empty(self):
        return len(self.__elements) == 0

    # Returns the element at the top of the stack
    # without removing it from the stack.
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__elements[-1]

    # Stores an element into the top of the stack
    def push(self, value):
        self.__elements.append(value)

    # Removes the element at the top of the stack and returns it
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.__elements.pop()

    # Return the size of the stack
    def __len__(self):
        return len(self.__elements)


class Node:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None  # Point to the right node, default None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root  # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:  # element matches current.element
                return True  # Element is found

        return False

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
            self.root = self.create_new_node(e)  # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False  # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.create_new_node(e)
            else:
                parent.right = self.create_new_node(e)

        self.size += 1  # Increase tree size
        return True  # Element inserted

    # Create a new TreeNode for element e
    def create_new_node(self, e):
        return Node(e)

    # Inorder traversal from the root
    def inorder(self):
        self.inorder_helper(self.root)

    # Inorder traversal from a subtree
    def inorder_helper(self, r):
        if r != None:
            self.inorder_helper(r.left)
            print(r.element, end=" ")
            self.inorder_helper(r.right)

    # Postorder traversal from the root parts of this code is from 'https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/'
    def postorder_iterative(self):

        # return if the tree is empty
        if self.get_root() is None:
            return None

        # create an empty stack and push the root node
        stack = Stack()
        stack.push(self.get_root())

        # create another stack to store postorder traversal
        out = Stack()

        # loop till stack is empty
        while stack:

            # pop a node from the stack and push the data into the output stack
            current = stack.pop()
            out.push(current.element)

            # push the left and right child of the popped node into the stack
            if current.left:
                stack.push(current.left)

            if current.right:
                stack.push(current.right)

        # print postorder traversal
        while out:
            print(out.pop(), end=" ")

    # Preorder traversal from the root
    def preorder(self):
        self.preorder_helper(self.root)

    # Preorder traversal from a subtree
    def preorder_helper(self, root):
        if root != None:
            print(root.element, end=" ")
            self.preorder_helper(root.left)
            self.preorder_helper(root.right)

    # Returns a path from the root leading to the specified element
    def path(self, e):
        list = []
        current = self.root  # Start from the root

        while current != None:
            list.append(current)  # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return list  # Return an array of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree
    def delete(self, e):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current != None:
            if e < current.element:
                parent = current
                current = current.left
            elif e > current.element:
                parent = current
                current = current.right
            else:
                break  # Element is in the tree pointed by current

        if current == None:
            return False  # Element is not in the tree

        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                self.root = current.right
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right  # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            # Eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                # Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left

        self.size -= 1
        return True  # Element deleted

    # Return true if the tree is empty
    def is_empty(self):
        return self.size == 0

    # Remove all elements from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def get_root(self):
        return self.root

    # Return the size of the tree
    def __len__(self):
        return self.size


if __name__ == "__main__":

    """ Test tree:
               8
              / \
             /   \
            3    10
           / \     \
          /   \     \
         1     6    14
              / \     \
             /   \     \ 
            4     7    20
    """
    # Print of this tree should be: 1, 4, 7, 6, 3, 20, 14, 10, 8

    # Test tree
    bst = BST()
    lis = [8, 3, 1, 6, 4, 7, 10, 14, 20]

    for i in lis:
        bst.insert(i)

    # Prints the correct post order of the binary tree
    bst.postorder_iterative()
