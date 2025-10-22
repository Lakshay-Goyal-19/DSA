# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # if not root or (not root.left and not root.right):
        #     return -1
        # left , right = root.left.val , root.right.val
        # if left == root.val:
        #     left = self.findSecondMinimumValue(root.left)
        # if right == root.val:
        #     right = self.findSecondMinimumValue(root.right)
        # if left != -1 and right != -1:
        #     return min(left, right)
        # if left != -1:
        #     return left
        # else:
        #     return right
        def inorder(node,ans):
            if not node:
                return 
            inorder(node.left , ans)
            ans.append(node.val)
            inorder(node.right , ans)
            return ans
        ans = []
        inorder(root,ans)
        ans.sort()
        unique = sorted(set(ans))
        if len(unique) < 2:
            return -1
        return unique[1]