class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {}
        d2 = {}
        ans = []
        min_sum = float('inf')
        for i in range(len(list1)):
            d1[list1[i]] = i
        for i in range(len(list2)):
            d2[list2[i]] = i
        for char,count in d1.items():
            if char in d2:
                total = count + d2[char]
                if total < min_sum:
                    min_sum = total
                    ans = [char]
                elif total == min_sum:
                    ans.append(char)
        return ans
        