# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:#if both are None then it is ok
            return True
        if p is None or q is None:#when one is None but the other is not
            return False
        if(p.val != q.val):
            return False
        lefttree = self.isSameTree(p.left , q.left)
        righttree = self.isSameTree(p.right , q.right)

        return lefttree and righttree
        