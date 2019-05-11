'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        index = 0
        while index<=right:
            if nums[index]==0 :
                nums[index],nums[left]=nums[left],nums[index]
                index+=1
                left+=1
            elif nums[index]==2:
                nums[index],nums[right]=nums[right],nums[index]
                right-=1
            else:
                index+=1
#三路快排,遇到nums[index]=0时,就把该元素与nums[left]交换,index+=1,left+=1;
#            nums[index]=1时,left,right不变,index+=1
#            nums[index]=2时,就把该元素与nums[right]交换,right-=1
