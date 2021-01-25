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
        if end==beg and nums[end]==target:
            return 1
        return 0


