# 79. Word Search

# Given a 2D board and a word, find if the word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cell,
#where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
       # check the bound
        if board == None or len(board) < 1:
            return False

        find_or_not = False

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                find_or_not = self.helper()
                if find_or_not:
                    return True
        return False

    def helper(self, board, i,j ,pos, word):
        # check if we have already check all the value
        if pos >= len(word):
            return True
        n = len(board)
        m = len(board[0])
        # check bound



