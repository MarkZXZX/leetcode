'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
'''

'''
解法：斐波那契 DP 使用迭代实现
'''
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        f0 = 1
        f1 = 1
        for i in range(2,n+1):
            temp = f0+f1
            f0 = f1
            f1 = temp
        return f1%1000000007