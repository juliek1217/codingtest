# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = n + 1
        fast = head
        while temp:
            if not fast:
                head = head.next
                return head
            fast = fast.next
            temp -= 1
        slow = head
        if fast:
            while fast:
                fast = fast.next
                slow = slow.next
        slow.next = slow.next.next
        return head
