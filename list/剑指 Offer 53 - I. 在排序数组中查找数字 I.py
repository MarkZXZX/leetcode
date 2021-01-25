'''
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
'''

'''
思路：使用二分查找法
end需要end-1，然后对于找不到的进行一个处理（否则死循环）
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        end = len(nums)-1
        beg = 0
        mid = (end+beg) / 2
        while end > beg:
            print(beg,end,mid)
            if nums[mid] == target:
                k1 = 1
                k2 = 1
                count = 1
                while(mid-k1>=0 and nums[mid-k1]==target):
                    count+=1
                    k1+=1
                while(mid+k2<len(nums) and nums[mid+k2]==target):
                    count+=1
                    k2+=1
                return count
            elif nums[mid]>target:
                end = mid
                mid = (end+beg)/2
            else:
                beg = mid+1
                mid = (end+beg)/2
        if end==beg and nums[end]==target: # 对于找不到的情况的处理或者最后一个就是的
            return 1
        return 0


