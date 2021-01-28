'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
'''

'''
解法：
一个很简单的DP算法
f(i) = f(i-2) + f(i-1)
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f1 = 1
        f2 = 2
        if n == 1:
            return f1
        elif n == 2:
            return f2

        for i in range(3,n+1,1):
            temp = f1 + f2
            f1 = f2
            f2 = temp
        return f2