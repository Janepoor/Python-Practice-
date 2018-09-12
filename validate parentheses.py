
# 20 Valid parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # using a stack

        stack = []

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                else:

                    if i == '}' and stack.pop() != '{' or i == ')' and stack.pop() != '(' or i == ']' and stack.pop() != '[':
                        return False

        return stack == []