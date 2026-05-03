# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rview(self, Depth : int , viewArr : [], node):
        curDepth = depth + 1
        arr = viewArr

        if curDepth > len(arr):
            arr.append(node.val)

        if node.right:
            arr = rview(curDepth, arr, node.right)
        if node.left:
            arr = rview(curDepth, arr, node.left)
        return arr

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            def rview(Depth : int , viewArr : [], node):
                curDepth = Depth + 1
                arr = viewArr

                if curDepth > len(arr):
                    arr.append(node.val)

                if node.right:
                    arr = rview(curDepth, arr, node.right)
                if node.left:
                    arr = rview(curDepth, arr, node.left)
                return arr
            if not root:
                return []
            return rview(0,[],root)