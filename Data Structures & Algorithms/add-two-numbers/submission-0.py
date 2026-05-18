# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ordinals = []

        head1 = l1
        head2 = l2

        while head1 or head2:
            num1 = 0
            num2 = 0
            if head1:
                num1 = head1.val
                head1 = head1.next
            
            if head2:
                num2 = head2.val
                head2 = head2.next

            ordinals.append(num1 + num2)

        dummyhead = ListNode()
        head = dummyhead
        remain = 0


        for val in range(len(ordinals)):
            if remain == 1:
                ordinals[val] += 1
                remain = 0

            if ordinals[val] >= 10:
                remain = 1
                ordinals[val] = ordinals[val] - 10 


            head.next = ListNode(ordinals[val])
            head = head.next


        if remain == 1:
            head.next = ListNode(1)

        return dummyhead.next



            


            