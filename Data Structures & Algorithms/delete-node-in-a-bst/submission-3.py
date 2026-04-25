# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self,root):
        curr = root

        while curr and curr.left:
            curr = curr.left

        return curr
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #first we need to fid the node we are deleting while tracking the parent node.
        if root == None:
            return None

        if key > root.val:      #these 2 section trverse the BST till the key is found.
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:

            if not root.left:
                return root.right #by returning the next node and not this one the current node is removed

            if not root.right:
                return root.left

            else:
                M = self.findMinNode(root.right)
                root.val = M.val
                root.right = self.deleteNode(root.right, M.val)
        return root


        

            