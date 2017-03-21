class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for n in range(len(nums)):
            hash[nums[n]] = n

        for key, position in hash.iteritems():
            if (target - key) in hash:

                print [position, hash[target - key]]


s=Solution()

s.twoSum([3,2,4], 6)

