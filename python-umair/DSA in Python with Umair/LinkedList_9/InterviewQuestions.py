# Interview Question on Linked List
from random import randint

class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
    
    def __str__(self):
        value = [str(x.value) for x in self]
        return ' -> '.join(value)
    
    def __len__(self):
        result = 0
        currNode = self.head
        while currNode:
            result += 1
            currNode = currNode.next
        return result

    def add(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
            self.length += 1
        
    def generate(self, n, miniValue, maxValue):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(miniValue, maxValue))
        return self

    def remove_duplicates(ll):
        if ll.head is None or ll.head.next is None:
            # Empty list or single-node list: no duplicates
            return ll.head        
        # Set to track unique values
        seen_values = set()        
        # Initialize pointers
        current = ll.head
        seen_values.add(current.value)  # Add the first node's value to the set
        while current.next:
            if current.next.value in seen_values:
                # Duplicate found; skip the node
                current.next = current.next.next
            else:
                # Add the value to the set and move forward
                seen_values.add(current.next.value)
                current = current.next
        return ll.head  # Return the head of the modified linked list

    # in this function we will find the nth node from the last
    # we assume that this is a singly linked list
    # with unknown length
    def nthfromLast(self, n):
        p = self.head
        q = self.head
        for i in range(n):
            if q is None:
                return None
            q = q.next
        while q is not None:
            p = p.next
            q = q.next
        return p
    
    # here we will partion the linkedlist around a given value
    # only for non circular linkedlist
    def partition(self,value):
        currNode = self.head
        self.tail = currNode
        nextNode = currNode.next
        currNode.next = None
        while nextNode:
            temp = nextNode.next
            if nextNode.value < value:
                nextNode.next = self.head
                self.head = nextNode
            else:
                self.tail.next = nextNode
                self.tail = nextNode
            nextNode = temp

# LL = LinkedList()
# LL.generate(10, 0, 30)
# print(LL) # 10 -> 20 -> 30 -> 20 -> 10 -> 20 -> 10 -> 10 -> 10 -> 20
# print(len(LL)) # 10

# # LL.remove_duplicates()
# # print(LL) 

# LL.partition(15)
# print(LL)

first = LinkedList()
first.add(7)
first.add(1)
first.add(6)
print(first)

second = LinkedList()
second.add(5)
second.add(9)
second.add(2)
second.add(1)
print(second)

def add_linked_lists(first, second):
    if first.head is None:
        return second
    if second.head is None:
        return first
    if first.head is None and second.head is None:
        return None 
    n1 = first.head
    n2 = second.head
    carry = 0
    ans = LinkedList()
    while n1 or n2:
        if n1 is None:
            a = 0
        else:
            a = n1.value
        if n2 is None:
            b = 0
        else:
            b = n2.value
        sum = a + b + carry
        carry = sum // 10
        ans.add(sum % 10)
        n1 = n1.next if n1 else None
        n2 = n2.next if n2 else None
    if carry > 0:
        ans.add(carry)
    return ans

ans = add_linked_lists(first, second)
print(ans)

# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-circular.
l1 = LinkedList()
l2 = LinkedList()
# adding the l1 nodes
l1.add(3)
l1.add(1)
l1.add(5)
l1.add(6)
l1.add(7)
l1.add(8)
# adding l2 nodes
l2.add(9)
l2.add(19)
l2.tail.next = l1.head.next.next.next.next # make an intersection
l2.tail = l1.tail
l2.length = 3
print(l2.head.value)
print(l1) # 3 -> 1 -> 5 -> 6 -> 7 -> 8
print(l2) # 9 -> 19 -> 7 -> 8
print(l1.length) # 5
print(l2.length) # 3

def check_intersection(first, second):
    # checking the tails is same ?
    if first.tail != second.tail:
        return False
    # retrieving the tail of the given linkedlists
    len1 = first.length
    len2 = second.length
    # getting the heads of the linkedlists
    temp1 = first.head
    temp2 = second.head
    # if the length of the first linkedlist is greater than the second one
    # then we will move the temp1 to the difference of the lengths
    if len1 >= len2:
        for i in range(len1 - len2):
            temp1 = temp1.next
    else:
        for i in range(len2 - len1):
            temp2 = temp2.next
    # now we will move both the pointers until they are equal
    while temp1 and temp2:
        if temp1 == temp2:
            return temp1 # return the intersecting node
        temp1 = temp1.next
        temp2 = temp2.next
    return None # if no intersection found

print(check_intersection(l1, l2)) # 7