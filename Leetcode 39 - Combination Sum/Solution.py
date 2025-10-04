class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i,path,sum):
            if sum == target:
                result.append(path[:])
                return
            if sum > target or i >= len(candidates):
                return
            path.append(candidates[i])
            dfs(i,path,sum + candidates[i])
            path.pop()
            dfs(i+1,path,sum)
        dfs(0,[],0)
        return result