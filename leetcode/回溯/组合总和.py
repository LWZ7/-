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
        candidates = sorted(candidates)
        
        def helper(temp , index):
            if sum(temp)>target or index==n:
                return
            if sum(temp)==target:
                res.append(temp)
                return
            helper(temp+[candidates[index]] , index)
            #排序后，如果有一个组合是大于target的，那么这个组合后面的数都不需要再试了
            #比如[2 , 2 ,6]大于7，那么不需要再尝试[2 , 2 , 7]了
            if sum(temp+[candidates[index]])<target:
                #这一步是回退，尝试用别的数，所以不应该把[candidates[index]]加上，index需要加1
                helper(temp , index+1)
        
        helper([] , 0)
        return res
        
#首先判断列表元素的和是不是大于目标数了，并且判断是否遍历到了总列表的最后一个元素，符合条件的话直接退出
#第二步才是判断如果列表和等于目标数的话,就把列表添加到结果列表中
#第三步,假设一直用同一个元素，有没有可能等于目标
#第四步，假设同一个数的和大于目标数，回退，尝试其他元素
