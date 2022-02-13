class Solution:
    def subsets(self, nums):
        ans = []
        ''' use depth-first-search to create the subset '''

        def dfs(left, current):
            if (left == len(nums)):
                ans.append(current)
                return
            dfs(left+1, current)
            dfs(left+1, current + [nums[left]])

        dfs(0, [])
        return ans
