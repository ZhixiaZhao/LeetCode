# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive
        
        # Base case:
        # both is null, True (null, null)
        # one has value, other one doesn't have, False (null, 6)
        # both has the same value, True (2, 2)
        # one has value, other one has other value, False (2, 3)
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # if p and q:
        #     if p.val == q.val:
        #         return True
        #     elif p.val != q.val:
        #         return False
        #     else:
        #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # else:
        #     return False
        