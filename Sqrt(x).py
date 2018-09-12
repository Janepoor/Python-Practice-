class Solution(object):
    def mySqrt_with_newton_method(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            r = (r + x / r) / 2

        return r

    def mySqrt(self, x):
        start, end = 1, x

        while start <= end:
            mid = start + (end - start) / 2

            if mid <= x / mid:
                start = mid + 1
            else:
                end = mid - 1

        return start - 1
