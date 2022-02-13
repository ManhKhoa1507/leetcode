class Solution:
    def twoSum(self, nums, target):
        ans = {}
        
        for i, num in enumerate (nums):
            t = target - num
            if t not in ans:
                ans[num] = i
            else:
                return [ans[t],i]

a = [3,2,4]
target = 6
print(Solution.twoSum(a,a,target))

