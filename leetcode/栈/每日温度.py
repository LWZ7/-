'''
根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高的天数。如果之后都不会升高，请输入 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的都是 [30, 100] 范围内的整数。
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = list()
        t_length = len(T)
        res_list = [0 for _ in range(t_length)]
        
        for key, value in enumerate(T):     
            if stack:
                while stack and T[stack[-1]] < value:
                    res_list[stack[-1]] = key - stack[-1]
                    stack.pop()
            stack.append(key)
        return res_list
#维护一个单调栈，保存还在递减中的值的索引，等到遇到大于栈顶元素的值时，再从栈中取出，并记录
