def twoSum(self, nums, tarset):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            a = tarset - nums[i]
            if (a in nums) and (nums.index(a) != i):
                return i, nums.index(a)