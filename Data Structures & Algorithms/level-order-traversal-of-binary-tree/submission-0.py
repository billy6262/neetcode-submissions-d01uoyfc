# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class levNode():
    def __init__(self,l,n):
        self.level = l
        self.node = n
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = [levNode(0,root)]
        retArr = []

        while len(nodes) > 0:
            if nodes[0].node.left:
                nodes.append(levNode(nodes[0].level + 1 ,nodes[0].node.left))

            if nodes[0].node.right:
                nodes.append(levNode(nodes[0].level + 1, nodes[0].node.right))

            if len(retArr) -1 >= nodes[0].level :
                retArr[nodes[0].level].append(nodes.pop(0).node.val)
            else:
                retArr.append([])
                retArr[nodes[0].level].append(nodes.pop(0).node.val)
        return retArr

            