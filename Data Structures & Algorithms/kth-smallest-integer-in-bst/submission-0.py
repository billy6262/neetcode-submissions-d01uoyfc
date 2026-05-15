# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None
        
        def DFS(root):
            if self.result != None or not root:
                return

            DFS(root.left)

            self.count += 1
            if self.count == k:
                self.result = root.val
                return

            DFS(root.right)

        DFS(root)
        return self.result

            


            

