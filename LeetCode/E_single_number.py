class Solution:
    def singleNumber(self, nums):
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        return xor
