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
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_x, max_y, max_step = len(board)-1, len(board[0])-1, len(word)-1
        def maze(x, y,step,visited):
            if visited[x][y]==1:
                return False
            if board[x][y] != word[step]:
                return False
            if step==max_step:
                return True
            visited[x][y]=1
            if x < max_x and maze(x+1,y,step+1,visited):
                return True
            if x>0 and maze(x-1,y,step+1,visited):
                return True
            if y<max_y and maze(x,y+1,step+1,visited):
                return True
            if y>0 and maze(x,y-1,step+1,visited):
                return True
            # 记得失败后要置零
            visited[x][y]=0
            return False
        visited=[[0]*(max_y+1) for _ in range(max_x+1)]
        for x in range(max_x+1):
            for y in range(max_y+1):
                if board[x][y] != word[0]:
                    continue
                if maze(x,y,0,visited):
                    return True
        return False
