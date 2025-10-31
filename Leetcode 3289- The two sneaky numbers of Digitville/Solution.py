class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1
            if(d[n] > 1):
                ans.append(n)
        return ans  