class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        ans = 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
        odd = False
        for count in d.values():
            if count % 2 == 0:
                ans += count
            else:
                ans += count -1
                odd = True
        if odd:
            ans += 1
        return ans