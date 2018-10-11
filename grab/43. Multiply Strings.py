# https://leetcode.com/problems/multiply-strings/description/


# key point num1[i], num2[j] will be placed at indices at [i+j. i+j + 1]
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == None or num2 == None:
            return

        m  = len(num1)
        n = len(num2)

        pos = [0 for _ in range(m+n)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i+j
                p2 = i+j + 1
                sum = mul + pos[p2]
                pos[p1]  += sum/10
                pos[p2] = sum % 10

        pt = 0
        while pt < len(pos) - 1 and pos[pt] == 0:
            pt += 1

        return ''.join(map(str, pos[pt:]))



