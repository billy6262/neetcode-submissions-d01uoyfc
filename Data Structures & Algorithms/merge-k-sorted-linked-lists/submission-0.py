# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyHead = ListNode()
        Tail = dummyHead


        while any(node is not None for node in lists):
            m_idx = -1
            for i, node in enumerate(lists):
                if node is not None and (m_idx == -1 or node.val < lists[m_idx].val):
                    m_idx = i
            
            m = lists[m_idx]
            Tail.next = m
            Tail = m
            lists[m_idx] = m.next


        return dummyHead.next