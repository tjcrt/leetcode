class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 1:
            return False
        ret = {}
        for i in range(len(nums)):
            if nums[i] in ret:
                return [ret[nums[i]], i]
            else:
                ret[target - nums[i]] = i