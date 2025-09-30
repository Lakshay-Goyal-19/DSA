# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if(self.same(root,subRoot)):
            return True
        lefttree = self.isSubtree(root.left , subRoot)
        righttree = self.isSubtree(root.right , subRoot)
        return lefttree or righttree

    def same(self,p,q):#this is to check if two trees are equal or not
    #helper function
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if(p.val != q.val):
            return False
        return self.same(p.left , q.left) and self.same(p.right , q.right)


        