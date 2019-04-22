'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    res = []
    def helper(self , nums , start):
        a = list(nums)
        b = len(nums)
        if start == b:
            self.res.append(a)
        else:
            for i in range(start , b):
                if i!=start and nums[i]==nums[start]:
                    continue
                #为什么要有这个if判断？
                a[i],a[start] = a[start],a[i]
                c = tuple(a)
                self.helper(c , start+1)#为什么是start+1？
                a[i],a[start] = a[start],a[i]
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.helper(tuple(nums) , 0)
        return self.res
