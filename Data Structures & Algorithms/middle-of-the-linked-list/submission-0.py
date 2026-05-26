# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while True:
            if not fast.next:
                return slow
            else:
                fast = fast.next

            if not fast.next:
                return slow.next
            else:
                fast = fast.next
                
            slow = slow.next
        