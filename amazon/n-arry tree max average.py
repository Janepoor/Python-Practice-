# https://cyqz.wordpress.com/2016/10/02/amazon-oa2-%E5%91%98%E5%B7%A5%E6%9C%80%E5%A4%A7%E5%B9%B3%E5%9D%87%E5%B7%A5%E4%BD%9C%E6%97%B6%E9%97%B4%EF%BC%88%E6%9C%80%E5%A4%A7%E5%B9%B3%E5%9D%87%E5%AD%90%E6%A0%91%EF%BC%89/

# return the maximum average


class Pair(object):

    def __init__(self, value, num, sum):
        self.value = value
        self.num = num
        self.sum = sum



def maxAveTime(node):
    res = node

    if node == None:
        return node
    pair = Pair(0,0,0)
    p = helper(node,res,pair)
