'''
给你一个整数数组 nums，请编写一个能够返回数组 “中心索引” 的方法。

数组 中心索引 是数组的一个索引，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，返回 -1 。如果数组有多个中心索引，应该返回最靠近左边的那一个。

注意：中心索引可能出现在数组的两端。

 

示例 1：

输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
索引 3 (nums[3] = 6) 的左侧数之和 (1 + 7 + 3 = 11)，与右侧数之和 (5 + 6 = 11) 相等。
同时, 3 也是第一个符合要求的中心索引。
'''

'''
解法：
简单的优化，去掉了重复的计算
'''
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return -1
        if sum(nums[1:]) == 0:
            return 0
        left = nums[0]
        right = sum(nums[2:])
        for i in range(1,len(nums)-1):
            if left == right:
                return i
            else:
                left += nums[i]
                right -= nums[i+1]
        if sum(nums[:-1]) == 0:
            return len(nums)-1
        return -1


            
