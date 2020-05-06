# linked_list.py
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================

# Evan McKague
# CS261

'''
**********************************************************************************
Part1: Deque and Bag implemented with Linked List
**********************************************************************************
'''

class SLNode:
    def __init__(self):
        self.next = None
        self.data = None


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a head and tail node with None data
        """
        self.head = SLNode()
        self.tail = SLNode()
        self.head.next = self.tail

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just return []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        cur = self.head

        # if index == 1:
        #     cur = cur.next
        #     new_link.next = cur.next
        #     cur.next = new_link

        # else:
        for i in range(index):
            cur = cur.next
        new_link.next = cur.next
        cur.next = new_link

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        cur = self.head
        if index == 0:
            temp = cur.next
            cur.next = temp.next
        else:
            for i in range(index):
                cur = cur.next
            temp = cur.next
            cur.next = temp.next

    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        cur = self.head

        temp = cur.next
        new_link.next = temp
        cur.next = new_link

    def add_back(self, data):
        """
        Adds a new node before the tail that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        cur = self.head

        while cur.next != self.tail:
            cur = cur.next

        new_link.next = self.tail
        cur.next = new_link

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        cur = self.head

        if cur.next == None:
            return None
        else:
            return cur.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """
        cur = self.head

        if cur.next == None:
            return None
        else:
            while cur.next != self.tail:
                cur = cur.next
            return cur.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        self.remove_link(0)

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        cur = self.head
        next = cur.next
        while next.next != self.tail:
            cur = cur.next
            next = cur.next

        cur.next = self.tail

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        cur = self.head

        if cur.next.data == None:
            return True
        else:
            return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        cur = self.head

        while cur.next != self.tail:
            cur = cur.next
            if cur.data == value:
                return True

        return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        cur = self.head
        i = 0
        while cur.next != self.tail:
            cur = cur.next
            if cur.data == value:
                self.remove_link(i)
            else:
                i += 1

    def show_list(self):

        cur = self.head
        while cur != self.tail:
            cur = cur.next
            if cur.data != None:
                print(cur.data)
        print("End of list.\n")


# Ll = LinkedList()
#
# Ll.add_front(5)
# Ll.add_front(4)
# Ll.add_back(6)
# print(Ll.__str__())
# print("-----")
# Ll.add_link_before(7, 2)
# print("added 7 before index 4")
# print(Ll.__str__())
# Ll.add_link_before(2, 0)
# print("added 2 to start")
# print(Ll.__str__())
# Ll.add_link_before(3, 1)
# print("added 3 to before index 1")
# print(Ll.__str__())
# print(Ll.contains(5))
# print(Ll.contains(6))
# print("-----")
# Ll.show_list()


'''
**********************************************************************************
Part 2: Deque implemented with CircularlyDoublyLinked List
**********************************************************************************
'''


class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a single sentinel node containing None data
        """
        self.sentinel = DLNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 <-> value2 <-> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.sentinel.prev != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.data)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        cur = self.sentinel

        if index == 0:
            cur = cur.next
            prev = self.sentinel
            new_link.next = cur
            new_link.prev = prev
            cur.prev = new_link
            prev.next = new_link

        else:
            for i in range(index+1):
                # print("add_link_before, i value:", i)
                cur = cur.next

            prev = cur.prev
            new_link.next = cur
            new_link.prev = prev
            cur.prev = new_link
            prev.next = new_link


    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        cur = self.sentinel

        if self.is_empty():
            return "list is empty"

        if index == 0:
            cur = cur.next
            prevnode = cur.prev
            nextnode = cur.next
            nextnode.prev = prevnode
            prevnode.next = nextnode
        else:
            i = 0
            while cur.next != self.sentinel and i <= index:
                cur = cur.next
                i += 1
            if i == index:
                return print("Exception: Index is out of bounds")
            else:
                prevnode = cur.prev
                nextnode = cur.next

                nextnode.prev = prevnode
                prevnode.next = nextnode



    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        self.add_link_before(new_link.data, 0)

    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        cur = self.sentinel
        i = 0
        while cur.next is not self.sentinel:
            cur = cur.next
            i += 1

        self.add_link_before(new_link.data, i)

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        if self.is_empty():
            return None
        else:
            return self.sentinel.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        cur = self.sentinel
        if self.is_empty():
            return None
        else:
            while cur.next != self.sentinel:
                cur = cur.next

        return cur.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        self.remove_link(0)

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        cur = self.sentinel
        i = 0
        while cur.next is not self.sentinel:
            cur = cur.next
            i += 1

        self.remove_link(i-1)

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        if self.sentinel.next == self.sentinel:
            return True
        else:
            return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        cur = self.sentinel

        while cur.next != self.sentinel:
            cur = cur.next
            if cur.data == value:
                return True

        return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        cur = self.sentinel
        i = 0
        while cur.next != self.sentinel:
            cur = cur.next
            if cur.data == value:
                self.remove_link(i)
            else:
                i += 1

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new links to do so.
        (e.g. you cannot call DLNode()). If the list printed by following next was 0, 1, 2, 3,
        after the call it will be 3,2,1,0
        """



        lastnode = self.sentinel.prev
        cur = lastnode


        while cur.prev != lastnode:
            prev = cur.prev
            cur.prev = cur.next
            cur.next = prev
            cur = prev

        return

# cList = CircularList()
# print("TEST CASES")
# print("add_link_before tests")
# cList.add_link_before(9, 0)
# cList.add_link_before(8, 0)
# cList.add_link_before(7, 0)
# cList.add_link_before(10, 3)
# print(cList.__str__())
# print("List should be:[7 <-> 8 <-> 9 <-> 10]")
# print("remove test cases")
# cList.remove_link(3)
# cList.remove_link(1)
# cList.remove_link(0)
# cList.remove_link(0)
# print(cList.__str__())
# print("List should be:[]")
# print("is empty test, it should be True")
# print(cList.is_empty())
# print("add front and back tests")
# print("List should be:[7 <-> 8 <-> 9 <-> 10]")
# cList.add_front(8)
# cList.add_front(7)
# cList.add_back(9)
# cList.add_back(10)
# print(cList.__str__())
# print("REVERSE TEST")
# print("List should be:[10 <-> 9 <-> 8 <-> 7]")
# cList.circularListReverse()
# print(cList.__str__())
# print("test cases for get front and get back")
# print("should return 7 and 10")
# print(cList.get_front())
# print(cList.get_back())
# print("test cases remove back and front")
# print("List should be:[8 <-> 9]")
# cList.remove_back()
# cList.remove_front()
# print(cList.__str__())
# print("CONTAINS TEST")
# print("should return true")
# print(cList.contains(9))
# print("should return false")
# print(cList.contains(10))
# print("REMOVE VALUE TEST")
# print("should return [8]")
# cList.remove(9)
# print(cList.__str__())
