class Solution:
    def maxSubArray_recurse(self, nums):
        size = len(nums)
        maxee = nums[0]
        
        def max_in_range(i):
            nonlocal maxee
            if i < 0:
                return 0
            a = max_in_range(i-1) + nums[i]
            b = nums[i]
            k = max(a,b)
            if k > maxee:
                maxee = k
            return k
        
        max_in_range(size - 1)
        return maxee

    def maxSubArray_iter(self,nums):
        current_max = global_max = nums[0]
        size = len(nums)
        if size == 0:
            return None
        elif size == 1:
            return nums[0]
        for i in range(1, size):
            current_max = max(current_max + nums[i], nums[i])
            if current_max > global_max:
                global_max = current_max
        return global_max

