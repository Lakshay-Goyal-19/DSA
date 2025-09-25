class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        for num,count in d.items():
            if(count>len(nums)//2):
                return num

