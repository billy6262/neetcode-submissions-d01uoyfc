class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = []
        q.append((root, float('-inf'), float('inf')))

        while q:
            node, lower, upper = q.pop()

            if not (lower < node.val < upper):
                return False

            if node.left:
                q.append((node.left, lower, node.val))

            if node.right:
                q.append((node.right, node.val, upper))
        return True