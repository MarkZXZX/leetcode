class Solution(object):
    '''
    DB解法是i-1推出i，使用的是循环的方法实现这个功能
    下面是最经典的db
    int array[n] = {0};
    array[1] = 1;
    for (int i = 2; i < n; i++)
        array[i] = array[i-1] + array[i-2];
    '''

    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        out = arr[0]
        for i in range(1,len(arr),1):
            key = arr[i]
            out += key
            for j in range(i-1,-1,-1):
                if key > arr[j]:
                    key = arr[j]
                out += key
                 
        return ((out)%(pow(10, 9) + 7))

    