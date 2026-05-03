# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def DFS( node, total, array):
            if not node:
                return
            otal = total  + node.val

            if not node.left and not node.right:
                array.append(otal)

            DFS(node.left, otal,array)
            DFS(node.right, otal,array)

        if not root:
            return False

        array = []

        DFS(root, 0 , array)

        if targetSum in array:
            return True

        else:
            return False

            

            


        