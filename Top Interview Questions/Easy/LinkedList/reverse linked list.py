# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #         node = head
        #         if node == None:
        #             return node

        #         if node.next == None:
        #             self.head = node
        #             return node

        #         self.reverseList(node.next)
        #         q = node.next
        #         q.next = node
        #         node.next = None
        #         return self.head

        prev = None
        curr = head
        nextn = None
        while curr != None:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        return prev
