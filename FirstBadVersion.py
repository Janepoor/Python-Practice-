# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion():
    pass

class Solution(object):
    def firstBadVersion(self, n):
        if n == 1:
            return 1
        left = 1
        right = n

        while right > left:
            mid = left + (right - left) / 2

            if isBadVersion(mid):  ##     ooxxxxxxxx
                right = mid
            else:  ##     ooooooooxx
                left = mid + 1
        return right

        """
        :type n: int
        :rtype: int
        """



def main():
    pass



if __name__ == '__main__':
    main()

