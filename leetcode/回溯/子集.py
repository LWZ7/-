'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution: 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        n = len(nums)
        
        def helper(idx, temp_list):
            res.append(temp_list)
            for i in range(idx, n):
                helper(i + 1, temp_list + [nums[i]])
        
        helper(0, [])
        return res
#这种题一看就知道可以用回溯，但是怎么回溯就是一个比较难的问题，遍历的顺序要在所有情况都合适才行  
class Solution: 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        if not nums:
            return res
        def helper(nums):
            if len(nums)==0:
                res.append([])
            else:
                helper(nums[1:])
                n = len(res)
                for i in range(n):
                    res.append([nums[0]]+res[i])
        helper(nums)
        return res
#从《SICP》学到的第二种解法，在《SICP》中，只有列表一种数据结构，列表中的元素，除了第一个，就是其他
#在这道题上，SuSets([1,2,3]) = SuSet([2,3])+[1].append(SuSet([2,3]))
#而上一种解法，则是从一个空列表开始，不停地把原列表中的元素加进来
