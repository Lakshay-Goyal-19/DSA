# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node,ans):
            if not node:
                return 
            inorder(node.left , ans)
            ans.append(node.val)
            inorder(node.right , ans)
            return ans
        ans = []
        inorder(root,ans)
        return ans[k-1]