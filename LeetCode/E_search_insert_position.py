class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums))
            if target <= nums[i]:
                return i
        return i

    def searchInsert_logn(self, nums, target):
        l = 0
        r = len(nums) - 1
        if target > nums[r]:
            return r+1
        elif target < nums[l]:
            return 0
        while l <= r:
            m = (l+r)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return l
