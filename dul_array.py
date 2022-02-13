class Solution:
    def removeDuplicates(self, nums):
        i = 0
        n = len(nums)
        while(i < n-1):
            if(nums[i] == nums[i+1]):
                del nums[i+1]
                n = len(nums)
            else:
                i += 1
        return len(nums)

def removeDuplicates(self, nums):
    i = 0
    n = len(nums)
    while(i < n-1):
        if(nums[i] == nums[i+1]):
            del nums[i+1]
            n = len(nums)
        else:
            i += 1
    return len(nums)


a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expected = []
len_info = removeDuplicates(a, a)
