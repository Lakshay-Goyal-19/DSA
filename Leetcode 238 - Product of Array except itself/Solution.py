class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        # print(left) product to the left of i
        right = [1] * n

        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        # print(right) product to the right of i
        output = []
        for i in range(n):
            output.append(left[i]*right[i])
        return output 

        