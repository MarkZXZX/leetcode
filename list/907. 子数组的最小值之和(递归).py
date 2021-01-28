class Solution(object):
    '''
    递归的方法是自顶向下的方法，但是递归并不是只能解决DP问题（学习中，一直不太会DP，已经写成博客csdn+腾讯社区）
    '''

    def db_iteration(self, arr, out_list): 
        '''
        return的值是需要加入list的值
        '''
        if len(arr) == 1:
            out_list.append(arr[0])
            return
        key = arr[-1]
        out_list.append(key)
        for k in range(len(arr)-2,-1,-1):
            # out_list.append(min(arr[k:len(arr)]))
            if arr[k] < key:
                key = arr[k]
            out_list.append(key)
            
        self.db_iteration(arr[:-1],out_list)

    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        out = []
        self.db_iteration(arr, out)
        # print(out)
        return (sum(out)%(pow(10, 9) + 7))

    