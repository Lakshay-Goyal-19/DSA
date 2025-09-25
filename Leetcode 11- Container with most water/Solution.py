class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        left=0
        right=len(height)-1
        for i in range(len(height)):
            maxarea=max(maxarea,(right-left)*min(height[left],height[right]))
            if(height[left]>height[right]):
                right-=1
            else:
                left+=1
        return maxarea





        