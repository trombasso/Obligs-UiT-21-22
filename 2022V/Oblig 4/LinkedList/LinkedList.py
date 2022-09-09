"""   !!!   Denne oppgaven er skrevet sammen med Jørgen Nordås   !!!    """


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # Return the head element in the list
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element

    # Return the last element in the list
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Add an element to the beginning of the list
    def addFirst(self, e):
        newNode = Node(e)  # Create a new node
        newNode.next = self.__head  # link the new node with the head
        self.__head = newNode  # head points to the new node
        self.__size += 1  # Increase list size

        if self.__tail == None:  # the new node is the only node in list
            self.__tail = self.__head

    # Add an element to the end of the list
    def addLast(self, e):
        newNode = Node(e)  # Create a new node for e

        if self.__tail == None:
            self.__head = self.__tail = newNode  # The only node in list
        else:
            self.__tail.next = newNode  # Link the new with the last node
            self.__tail = self.__tail.next  # tail now points to the last node

        self.__size += 1  # Increase size

    # Same as addLast
    def add(self, e):
        self.addLast(e)

    # Insert a new element at the specified index in this list
    # The index of the head element is 0
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e)  # Insert first
        elif index >= self.__size:
            self.addLast(e)  # Insert last
        else:  # Insert in the middle
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node.
    def removeFirst(self):
        if self.__size == 0:
            return None  # Nothing to delete
        else:
            temp = self.__head  # Keep the first node temporarily
            self.__head = self.__head.next  # Move head to point the next node
            self.__size -= 1  # Reduce size by 1
            if self.__head == None:
                self.__tail = None  # List becomes empty
            return temp.element  # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None  # Nothing to remove
        elif self.__size == 1:  # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head

            for i in range(self.__size - 2):
                current = current.next

            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list.
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None  # Out of range
        elif index == 0:
            return self.removeFirst()  # Remove first
        elif index == self.__size - 1:
            return self.removeLast()  # Remove last
        else:
            previous = self.__head

            for i in range(1, index):
                previous = previous.next

            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0

    # Return the size of the list
    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", "  # Separate two elements with a comma
            # else:

        result += "]"  # Insert the closing ] in the string
        return result

    # Clear the list */

    def clear(self):
        current = self.__head
        while current is not None:
            current = current.next
            self.removeAt(0)
        self.__head = self.__tail = None

    # Return true if this list contains the element o
    def contains(self, e):
        if self.__size == 0:
            return False
        else:
            current = self.__head
            while current.element != e:
                current = current.next
                if current == None:
                    return False
            return True

    # Remove the element and return true if the element is in the list
    def remove(self, e):
        index = 0
        if self.__size == 0:
            return False
        else:
            current = self.__head
            while current.element != e:
                current = current.next
                index += 1
                if current == None:
                    return False
            self.removeAt(index)
            return True

    # Return the element from this list at the specified index
    def get(self, index):
        counter = 0
        if self.__size == 0:
            return False
        else:
            current = self.__head
            while counter != index:
                current = current.next
                counter += 1
                if current == None:
                    return False
            return current.element

    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def indexOf(self, e):
        if self.__size == 0:
            return -1
        else:
            counter = 0
            current = self.__head
            while current.element != e:
                current = current.next
                counter += 1
                if current is None:
                    return -1
            return counter

    # Return the index of the last matching element in this list
    #  Return -1 if no match.
    def lastIndexOf(self, e):
        if self.__size == 0:
            return -1
        else:
            counter = 0
            lastfound = -1
            current = self.__head
            while current != None:
                if current.element == e:
                    lastfound = counter
                current = current.next
                counter += 1
                if current is None:
                    return lastfound
            return lastfound

    # Replace the element at the specified position in this list
    #  with the specified element. */
    def set(self, index, e):
        counter = 0
        if self.__size == 0:
            return False
        else:
            current = self.__head
            while counter != index:
                current = current.next
                counter += 1
                if current == None:
                    return False
            current.element = e

    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)


"""  The Node class  """


class Node:
    def __init__(self, e):
        self.element = e
        self.next = None


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element


""" MAIN MAIN MAIN"""


def main():
    # Creating a list
    lst = LinkedList()
    lst.add("jørgen")
    lst.add("anders")
    lst.add("erik")
    lst.add("elias")
    lst.add("tjhomas")
    lst.add("erik")
    lst.add("konrad")
    lst.add("oluf")
    lst.add("kjartan")
    lst.add("birger")

    print(lst)  # Prints linked list

    # Checking if list contains "mohammed" and/or kjartan
    print(lst.contains("mohammed"))  # returns False
    print(lst.contains("kjartan"))  # returns True

    # Getting index of a node with set value
    print(lst.indexOf("oluf"))  # returns 7
    print(lst.indexOf("achmed"))  # returns -1

    # Getting idex of last node with set value similar to other nodes
    print(lst.lastIndexOf("erik"))  # returns 5
    print(lst.lastIndexOf("siri"))  # returns -1

    # Remove node determined by containing value
    print(lst.remove("konrad"))  # returns True
    print(lst.remove("kåre"))  # returns False

    # Return the element from this list at the specified index
    print(lst.get(0))  # Returns jørgen
    print(lst.get(18))  # Returns False

    # Change value of first node to "erik"
    lst.set(0, "erik")
    print(lst)  # Prints list. erik is now the first variable instead of jørgen

    # Clears the list
    lst.clear()
    print(lst)  # Only displays "[]"


if __name__ == "__main__":
    main()
