'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''
class Solution:
    def helper(self , nums , left , right , target):
        while left<=right:
            mid = left+int((right-left)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        point = 0
        
        #求最小值,必须是left<right,否则的话第一次mid就求到最小值就无解了
        while left < right:
            mid = left+int((right-left)/2)
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
        point = left
        
        ans = self.helper(nums , 0 , point-1 , target)
        if ans==-1:
            ans = self.helper(nums , point , n-1 , target)
            return ans
        else:
            return ans
