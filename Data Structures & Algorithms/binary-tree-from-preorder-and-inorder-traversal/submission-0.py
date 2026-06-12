class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderDict = dict()

        for i , val in enumerate(inorder):
            inorderDict[val] = i

        self.index = 0
        def DFS(l, r):
            if l > r:
                return
            rootval = preorder[self.index]
            rootindex = inorderDict[rootval]
            root = TreeNode(rootval)
            self.index += 1
            root.left = DFS(l,rootindex - 1)
            root.right = DFS(rootindex + 1,r)
            return root

        return DFS(0,len(preorder) - 1)