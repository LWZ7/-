'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
'''
class Solution:
    #第一种方法，保存当前数字，如果遇到相同数字，count+1，否则count-1，如果count=0，换一个数字
    def majorityElement(self, nums: List[int]) -> int:
        k = len(nums)
        count = 1
        if k == 0:
            return 
        m = nums[0]
        for i in range(1,k):
            if m == nums[i]:
                count+=1
            else:
                count-=1
                if count == 0:
                    m = nums[i+1]
        return m
    #第二种方法，排序
    def majorityElement(self, nums: List[int]) -> int:
        a = sorted(nums)
        return a[int(len(a)/2)]
