class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        min_heap=[]
        for num,count in d.items():
            heapq.heappush(min_heap,(count,num))
            if(len(min_heap)>k):
                heapq.heappop(min_heap)
        result=[]
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        return result





        