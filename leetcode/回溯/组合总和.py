'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        def helper(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return 
            if tmp_sum == target:
                res.append(tmp)
                return 
            helper(i,  tmp_sum + candidates[i],tmp + [candidates[i]])
            helper(i+1, tmp_sum ,tmp)
        helper(0, 0, [])
        return res
        
#首先判断列表元素的和是不是大于目标数了，并且判断是否遍历到了总列表的最后一个元素，符合条件的话直接退出
#第二步才是判断如果列表和等于目标数的话,就把列表添加到结果列表中
#第三步,假设一直用同一个元素，有没有可能等于目标
#第四步，假设同一个数的和大于目标数，回退，尝试其他元素
