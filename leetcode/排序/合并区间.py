'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []: return []
        
        intervals.sort(key=lambda x:x[0])  # 先按根据每个区间的第一项对列表进行排序
        res = [intervals[0]]   # 用于保存得到的结果区间
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:  # 如果某个区间的最小值比结果列表中的最后一个区间的最大值小，则更新结果中的最后一个区间
                res[-1] = [res[-1][0], max(intervals[i][1], res[-1][1])]
            else:                                          # 否则，将当前区间加入结果列表中
                res.append(intervals[i])
        
        return res
