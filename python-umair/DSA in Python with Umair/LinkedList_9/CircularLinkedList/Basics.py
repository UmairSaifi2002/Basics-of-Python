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
    

# # creating a circular singly linkedlist containing sinf
# csll = CircularSinglyLinkedList(1)

# # creating a circular singly linkedlist 
csll = CircularSinglyLinkedList()

csll.append(1)
csll.append(2)
csll.append(3)
csll.append(4)

print(csll)