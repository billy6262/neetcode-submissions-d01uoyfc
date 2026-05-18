# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        def DFSP(root):
            if root:
                DFSP(root.left)
                DFSP(root.right)
                ret.append(root.val)

        DFSP(root)
        return ret
