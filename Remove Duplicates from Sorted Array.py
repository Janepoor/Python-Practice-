class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0

        size = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[size]:
                size += 1
                nums[size] = nums[i]

        return size + 1

