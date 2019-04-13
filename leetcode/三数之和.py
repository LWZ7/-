'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        i = 0
        length =  len(nums)
        for i in range(length):
            if i==0 or nums[i]>nums[i-1]:
                left = i+1
                right = length-1
                while left < right:
                    s = nums[i]+nums[left]+nums[right]
                    if s == 0:
                        res.append([nums[i] , nums[left] , nums[right]])
                        left+=1
                        right-=1
                        #下面两个while循环是避免重复三元组进去
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while right>left and nums[right]==nums[right+1]:
                            right-=1
                    elif s > 0:
                        right -= 1
                    else:
                        left += 1
        return res
#从头到尾遍历一遍，然后每次遍历用一次双指针法,双指针循环中要加两个while循环，避免重复  
#if i==0 or nums[i]>nums[i-1]的作用也是为了防止重复
            
        
