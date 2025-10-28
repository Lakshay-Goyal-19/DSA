class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)
        right = 0
        ans = 0
        for i in range(len(nums)):
            right = total - left - nums[i]
            if nums[i] == 0:
                if left == right:
                    ans += 2
                if left + 1 == right or right + 1 == left:
                    ans += 1
            left += nums[i]
        return ans