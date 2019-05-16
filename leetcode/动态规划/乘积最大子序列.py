'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mid = [0,0]
        if nums[0] >= 0:
            mid = [0,nums[0]]
        else:
            mid = [nums[0],0]
        for i in range(1,len(nums)):
            if nums[i] >= 0:
                mid[1] = max(nums[i],nums[i]*mid[1])
                mid[0] = mid[0]*nums[i]
            else:
                mid[0],mid[1] = min(nums[i],nums[i]*mid[1]), nums[i]*mid[0]
            res = max(res,mid[1])
        return res
            
        
