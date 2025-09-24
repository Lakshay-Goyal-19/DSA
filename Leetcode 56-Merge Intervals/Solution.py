class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged=[]
        default=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=default[1]:
                default[1] = max(default[1], intervals[i][1])
            else:
                merged.append(default)
                default=intervals[i]
        merged.append(default)
        return merged
