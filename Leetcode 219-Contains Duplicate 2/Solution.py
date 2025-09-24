class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #TLE Solution
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]==nums[j]):
        #             if(abs(i-j)<=k):
        #                 return True
        # return False
        d={}
        for i in range(len(nums)):
            if(nums[i] not in d):
                d[nums[i]] = i
            elif(nums[i] in d):    
                if(abs(d.get(nums[i])-i) <= k):
                    return True
                else:
                    d[nums[i]] = i
        return False

      

