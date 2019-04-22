'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = len(nums)
        res = []
        left = 0
        right = a - 1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid]==target:
                if mid==0 or nums[mid-1]<target:
                    res.append(mid)
                    break
                else:
                    right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        left = 0
        right = a-1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] == target:
                if mid == a-1 or nums[mid+1]>target:
                    res.append(mid)
                    break
                else:
                    left+=1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        if len(res)!=2:
            return [-1,-1]
        else:
            return res
