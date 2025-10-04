class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        if not nums:
            return []
        pair = ""
        i = 0
        for j in range(1,len(nums)):
            if(nums[j] - nums[j-1] != 1):
                if i == j-1:
                    output.append(str(nums[i]))
                else:
                    pair = f"{nums[i]}->{nums[j-1]}"
                    output.append(pair)
                i = j
        if i == len(nums)-1:
            output.append(str(nums[i]))
        else:
            output.append(f"{nums[i]}->{nums[-1]}")
        return output


        