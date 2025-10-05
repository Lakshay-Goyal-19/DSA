# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque([root])
        while queue:
            sum1 = 0
            counter = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum1 = sum1 + node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                counter += 1
            average = sum1 / counter
            ans.append(average)
        return ans


        