

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False
        row, col = len(matrix), len(matrix[0])
        low, high = 0, row * col - 1

        while (low <= high):
            mid = (low + high) / 2
            num = matrix[mid / col][mid % col]
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


# class Solution(object):
#     def searchMatrix(self, matrix, target):
#
#         if len(matrix) == 0:
#             return False
#         for i in range(len(matrix)):
#             if len(matrix[i]) == 0:
#                 return False
#
#         row, column = len(matrix), len(matrix[0])
#         low, high = 0, row - 1
#
#         while (low <= high):
#             mid = low + (high - low) / 2
#             if matrix[mid][0] == target:
#                 return True
#             elif matrix[mid][0] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#
#         start, end = 0, column - 1
#         result = 0
#         while (start <= end):
#             mid2 = start + (end - start) / 2
#             if matrix[low - 1][mid2] == target:
#                 return True
#             elif matrix[low - 1][mid2] < target:
#                 start = mid2 + 1
#             else:
#                 end = mid2 - 1
#
#             result = mid2
#
#         if matrix[mid - 1][result] == target:
#             return True
#         else:
#             return False
