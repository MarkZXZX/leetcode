'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

解法：
二分查找的关键就是要找到一个跳出条件：因为基于len-1 0 加个mid很可能会卡死，
正确的是：len-1 加上 mid，但是对于查找：可能会出现不存在的情况，要写退出方法
对于这个题的问题，需要在足够小的时候（比如三个元素的时候）写出跳出程序

但是这个题很奇葩在于：居然重复，但是list(set(l))居然是打乱顺序的去重方法
'''
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        numbers = sorted(set(numbers),key=numbers.index)
        print(numbers)
        if numbers[-1] > numbers[0]:
            return numbers[0]
        beg = 0
        end = len(numbers)-1
        mid = (end+beg)/2
        while end>beg:
            print(beg,mid,end)
            if mid == beg:
                return min(numbers[beg],numbers[end])
            if numbers[mid] < numbers[mid+1] and numbers[mid] < numbers[mid-1]:
                return numbers[mid]
            if numbers[mid]>=numbers[beg]:
                beg = mid
                mid = (end+beg)/2
            else:
                end = mid
                mid = (beg+end)/2
        return numbers[mid]