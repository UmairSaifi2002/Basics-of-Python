class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.value} -> ", end="")
            current = current.next
        print("None")


# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# # Question 1. 
# # Merge Two Sorted Linked List
# # You are given the heads of two sorted linked lists list1 and list2. 

# # Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# # Return the head of the merged linked list.   

# class MergeTwoLinkedList:
#     def merge(self, l1, l2):
#         """
#         Merge two sorted linked lists into one sorted linked list.
#         """
#         temp = Node(-1)  # Dummy node to start the merged list
#         current = temp

#         # Merge the two lists while both have nodes
#         while l1 and l2:
#             if l1.value < l2.value:
#                 current.next = l1
#                 l1 = l1.next
#             else:
#                 current.next = l2
#                 l2 = l2.next
#             current = current.next

#         # Append the remaining nodes from either list
#         if l1:
#             current.next = l1
#         if l2:
#             current.next = l2

#         return temp.next  # Return the merged list, excluding the dummy node


# # Create and populate the first linked list
# l1 = LinkedList()
# l1.insert_at_end(1)
# l1.insert_at_end(2)
# l1.insert_at_end(4)

# # Create and populate the second linked list
# l2 = LinkedList()
# l2.insert_at_end(1)
# l2.insert_at_end(3)
# l2.insert_at_end(4)

# # Merge the two linked lists
# merger = MergeTwoLinkedList()
# merged_head = merger.merge(l1.head, l2.head)

# # Display the merged linked list
# print("Merged Linked List:")
# current = merged_head
# while current:
#     print(f"{current.value} -> ", end="")
#     current = current.next
# print("None")

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Question 2
# Remove Duplicates
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well. 

# class Solution(object):
#     def deleteDuplicates(self, head):
#         # TODO
#         if head is None:
#             return
#         values = set()
#         curr = head
#         values.add(curr.val)
#         while curr.next:
#             if curr.next.val in values:
#                 curr.next = curr.next.next
#             else:
#                 values.add(curr.next.val)
#                 curr = curr.next
#         return head

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Question 3
# Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# def removeElements(self, head, val):
#         # TODO
#         prev = ListNode(-1)
#         curr = head
#         prev.next = curr
#         H = prev
#         while curr:
#             if curr.val == val:
#                 prev.next = curr.next
#             else:
#                 prev = curr
#             curr = curr.next
#         return H.next

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

#  def reverseList(self, head):
#         # Solution goes here
#         if head is None:
#             return head
#         elif head.next is None:
#             return head
#         else:
#             prev = None
#             curr = head
#             Next = curr.next
#             while curr:
#                 curr.next = prev
#                 prev = curr
#                 curr = Next
#                 if Next:
#                     Next = Next.next
#             return prev

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Check Palindrome
# Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# class Palindrome:
#     def checkPalidrome(self,head):
#         if head == None:
#             return False
#         elif head != None and head.next == None:
#             return True
#         else:
#             curr = head
#             ls = []
#             while curr:
#                 ls.append(curr.value)
#                 curr = curr.next
#             # print(ls)
#             t = tuple(ls)
#             ls.reverse()
#             if list(t) == ls:
#                 return True
#             else:
#                 return False

# head = LinkedList()
# # head = None
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(1)
# # head.next.next.next = Node(4)

# p = Palindrome()
# print(p.checkPalidrome(head))

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# class find_middle:
#     def middleNode(self, head):
#         slow = head
#         fast = head
#         while fast is not None and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next
#         return slow.value

# m = find_middle()
# head = Node(0)
# head.next = Node(1)
# head.next.next = Node(2)
# head.next.next.next = Node(3)
# head.next.next.next.next = Node(4)

# print(m.middleNode(head))