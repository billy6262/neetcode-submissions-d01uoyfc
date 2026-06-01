# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        stack = []
        curr = root
        self.arr = []
        self.i = 0

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.arr.append(curr.val)
                curr = curr.right



    def next(self) -> int:
        ret = self.arr[self.i]
        self.i += 1
        return ret

    def hasNext(self) -> bool:
        if self.i < len(self.arr):
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()