"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def calcNext(root):
            if not root or root.left == None:
                return

            root.left.next = root.right

            if root.next:
                root.right.next = root.next.left

            calcNext(root.right)
            calcNext(root.left)\
        
        calcNext(root)

        return root

        