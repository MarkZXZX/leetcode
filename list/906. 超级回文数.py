'''
906. 超级回文数
如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。

现在，给定两个正整数 L 和 R （以字符串形式表示），返回包含在范围 [L, R] 中的超级回文数的数目。

输入：L = "4", R = "1000"
输出：4
解释：
4，9，121，以及 484 是超级回文数。
注意 676 不是一个超级回文数： 26 * 26 = 676，但是 26 不是回文数。
'''
'''
思路：
这个解法会出现内存不够的情况，但是是一个挺好的实现方法
'''
import math
import numpy as np
class Solution(object):
    def superpalindromesInRange(self, left, right):
        """
        :type left: str
        :type right: str
        :rtype: int
        """
        count = 0
        list_range = np.arange(int(left),int(right)+1)
        for i in list_range:
            str_i = str(i)
            start = len(str_i)/2 + 1 if len(str_i)%2 != 0 else len(str_i)/2
            if str_i[0:len(str_i)/2] == str_i[start:len(str_i)]:
                sqrt_num =  math.sqrt(i)
                if int(sqrt_num) == sqrt_num:
                    # print(sqrt_num,i)
                    str_sqrt = str(int(sqrt_num))
                    start = len(str_sqrt)/2 + 1 if len(str_sqrt)%2 != 0 else len(str_sqrt)/2
                    if str_sqrt[0:len(str_sqrt)/2] == str_sqrt[start:len(str_sqrt)]:
                        count += 1
        return count