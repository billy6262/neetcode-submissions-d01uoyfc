"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldnodes = {}
        dummy = Node(0)
        newhead = dummy
        oldhead = head 

        while oldhead != None:
            newhead.next = Node(oldhead.val)
            newhead = newhead.next

            oldnodes[oldhead] = newhead
            oldhead = oldhead.next

        oldhead = head

        while oldhead != None:
            newhead = oldnodes[oldhead]
            if oldhead.random:
                newhead.random = oldnodes[oldhead.random]
            oldhead = oldhead.next

        return dummy.next

            
