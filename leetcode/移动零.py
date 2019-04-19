'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # b = len(nums)
        # count = 0
        # while i < b:
        #     if count == b-1:
        #         break
        #     if nums[i]==0:
        #         if i!=0:
        #             i-=1
        #             del nums[i+1]
        #         else:
        #             del nums[i]
        #         nums.append(0)
        #         count+=1
        #     else:
        #         i+=1
        #         count+=1
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                count += 1
            else:
                i += 1
        for j in range(count):
            nums.append(0)
