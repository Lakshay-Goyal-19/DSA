class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        #this approach causes TLE because of the two loops
        # nums.sort()
        # used = set()
        # for i in nums:
        #     for j in range(i-k,i+k+1):
        #         if j not in used:
        #             used.add(j)
        #             break
        # return len(used)

        nums.sort()
        current = float('-inf') 
        count = 0
        for i in nums:
            candidate = max(current+1,i-k)
            if candidate <= i+k:
                count += 1
                current = candidate
        return count
        