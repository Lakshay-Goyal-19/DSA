class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxi = 0
        seen = {}
        max_freq = 0
        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right],0) + 1
            window_size = right - left + 1
            max_freq = max(max_freq , seen[s[right]])
            if(window_size - max_freq > k):
                seen[s[left]] -= 1
                left += 1
            maxi = max(maxi , right - left + 1)
        return maxi