class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        d2 = {}
        ans = []
        for i in range(len(nums1)):
            d1[nums1[i]] = d1.get(nums1[i],0) + 1
        for i in range(len(nums2)):
            d2[nums2[i]] = d2.get(nums2[i],0) + 1
        for num in d1.keys():
            if num in d2:
                ans.append(num)
        return ans