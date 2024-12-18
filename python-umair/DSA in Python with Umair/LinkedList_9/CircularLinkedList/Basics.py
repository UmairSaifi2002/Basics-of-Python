class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class CircularSinglyLinkedList:
    # we make a Circular linked list as a Empty
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # we make a Circular linked list using one Node
    # def __init__(self,value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            temp = temp.next
            if temp is self.head:
                break
            result += ' -> '
        result += ' -> self.head'
        return result

    def append(self,value):
        temp = Node(value)
        # if circular linked list is empty
        if self.length == 0:
            self.head = temp
            self.tail = temp
            temp.next = temp
        else:
            self.tail.next  = temp 
            self.tail = temp
            temp.next = self.head
        self.length += 1
    
    def prepend(self, value):
        temp = Node(value)
        if self.length == 0:
            self.head = temp
            self.tail = temp
            temp.next = temp
        else:
            temp.next = self.head
            self.head = temp
            self.tail.next = temp
        self.length += 1
    
    def insert(self,index,value):
        temp = Node(value)
        if 0 < index or index > self.length:
            print('Please Enter a valid index')
        # when Circular singly linkedlist is Empty
        if self.length == 0:
            self.head = temp
            self.tail = temp
            temp.next = temp
        else: # when Circular Singly Linkedlist have some Nodes
            if index == 0: # when you insert at the beginning of Circular singly linkedlist  
                temp.next = self.head
                self.head = temp
                self.tail.next = temp
            elif index == self.length: # when you insert at the last of Circular singly linkedlist
                self.tail.next = temp
                temp.next = self.head
                self.tail = temp
            else: # when you want to insert in between in the Circular LinkedList
                temp_node = self.head
                for _ in range(index-1):
                    temp_node = temp_node.next
                temp.next = temp_node.next
                temp_node.next = temp
        self.length += 1

    def POPFirst(self):
        self.length -= 1
        if self.length == 0:
            return 'Circular LinkedList is Empty'
        elif self.length == 1:
            first = self.head
            self.head = None
            self.tail = None
            return first.value
        else:
            first = self.head
            second = self.head.next
            self.tail.next = second
            self.head = second
            first.next = None
            return first.value
    
    def pop(self):
        Popped_Node = self.tail
        temp = self.head
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            return Popped_Node
        else:
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail.next = None
            self.tail = temp
        self.length -= 1
        return Popped_Node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        # When the list is empty
        if self.head is None:
            return None

        # Remove head
        if index == 0:
            popped = self.head
            self.head = self.head.next
            if self.length == 1:  # If it was the only node, update tail
                self.tail = None
            popped.next = None
            self.length -= 1
            return popped

        # Remove tail
        if index == self.length - 1:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            popped = self.tail
            temp.next = None
            self.tail = temp
            self.length -= 1
            return popped

        # Remove node in between
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        popped = temp.next
        temp.next = popped.next
        popped.next = None
        self.length -= 1
        return popped

    def deleteAll(self):
        self.tail.next = None
        self.tail = None
        self.head = None
        self.length = 0
        return None
    
    def search(self,target):
        temp = self.head
        while temp is not None:
            if temp.value == target:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False
    
    def GetNode(self,index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.head.value
        else:
            temp = self.head
            l = 0
            while temp is not None:
                if l == (index):
                    return temp
                temp = temp.next
                l += 1      

    def SetNodeValue(self, index, value):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            self.head.value = value
            return self.head
        else:
            temp = self.head
            l = 0
            while temp is not None:
                if l == index:
                    temp.value = value
                    return temp
                temp = temp.next
                l += 1
    
    # Split a Circular Linked List into Two Equal Halves
    # Write a function to split the circular linked list into two equal halves. If the list has odd number of nodes, 
    # the extra node should go to the first list. 
    def splitLinkedList(self):
        if self.length == 0:  # Empty list
            return None, None
        if self.length == 1:  # Single-node list
            firstList = CircularSinglyLinkedList()
            firstList.append(self.head.value)
            return firstList, None

        # Step 1: Find the middle using slow and fast pointers
        slow = self.head
        fast = self.head
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Create two new circular linked lists
        firstList = CircularSinglyLinkedList()
        secondList = CircularSinglyLinkedList()

        # Step 3: Populate the first list (from head to slow)
        temp = self.head
        while temp != slow.next:
            firstList.append(temp.value)
            temp = temp.next

        # Step 4: Populate the second list (from slow.next to end)
        temp = slow.next
        while temp != self.head:
            secondList.append(temp.value)
            temp = temp.next

        return firstList, secondList

    def is_sorted(self):
        if self.head is None:
            return True
        elif self.head.next is None:
            return True
        else:
            temp = self.head
            while temp.next is not self.head:
                if temp.value > temp.next.value:
                    return False
                temp = temp.next
            return True

    def insert_into_sorted(self, data):
        temp = Node(data)
        # case 1 - linked list is Empty
        if self.head is None:
            self.head = temp
            self.head.next = self.head
        # case 2 - Only one node is present in linked list
        elif self.head.next is None:
            if self.head.value <= data:
                self.head.next = temp
                temp.next = self.head
            else:
                temp.next = self.head
                self.head.next = temp
        else:
            temp = Node(data)
            # data <= self.head
            if data <= self.head.value:
                temp.next = self.head
                self.tail.next = temp
            # data >= self.tail
            elif data >= self.tail.value:
                self.tail.next = temp
                self.tail = temp
                temp.next = self.head
            # self.head < data < self.tail
            else:
                prev = None
                curr = self.head
                while data > curr.value :
                    prev = curr
                    curr = curr.next
                temp.next = curr
                prev.next =temp

# # creating a circular singly linkedlist 
csll = CircularSinglyLinkedList()

csll.append(1)
csll.append(2)
csll.append(3)
csll.append(4)

csll.prepend(0)

csll.insert(0,100)
csll.insert(6,100)
csll.insert(4,100)
csll.insert(10,100)
csll.insert(-4, 100)

print(csll.length)
print(csll)

print(csll.search(10))

print(csll.GetNode(2).value)
print(csll.GetNode(20))

print(csll.SetNodeValue(2,20))
print(csll)

print(csll.POPFirst())
print(csll)

print(csll.pop().value)
print(csll)

print(csll.remove(2).value)
print(csll) # 100 -> 20 -> 1 -> 2 -> 100 -> 3 -> 4 -> self.head

print(csll.GetNode(3).value)
print(csll.SetNodeValue(0,0).value)
print(csll.SetNodeValue(1,0.5).value)
print(csll.SetNodeValue(4,2.5).value)
print(csll) # 0 -> 0.5 -> 1 -> 2 -> 2.5 -> 3 -> 4 -> self.head

print(f'The CLL is  sorted ? -> {csll.is_sorted()}')