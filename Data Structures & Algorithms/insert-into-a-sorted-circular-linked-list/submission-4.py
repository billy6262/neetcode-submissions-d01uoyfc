class Solution:
    def insert(self, head: 'Optional[Node]', iVal: int) -> 'Node':
        if not head:
            n = Node(iVal)
            n.next = n
            return n
        cur = head

        while cur.next != head:
            # Standard insertion: between two nodes where cur <= iVal <= next
            if cur.val <= iVal <= cur.next.val:
                break
            # Edge case: cur is the tail (largest) and next is the head (smallest)
            if cur.val > cur.next.val:
                if iVal >= cur.val or iVal <= cur.next.val:
                    break
            cur = cur.next

        n = Node(iVal, cur.next)
        cur.next = n
        return head