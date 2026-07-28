# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Step 1: Find the center using slow/fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split the list and reverse the second half
        second = slow.next
        slow.next = None  # Disconnect the two halves
        
        # Reverse the second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Step 3: Interweave the two halves
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2