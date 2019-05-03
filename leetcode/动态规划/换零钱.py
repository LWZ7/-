'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1

分别用动态规划、深度优先、广度优先解决
'''
#动态规划
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [float('inf')]*(amount+1)
        mem[0] = 0
        
        for coin in coins:
            for j in range(coin, amount+1):
                if j-coin >= 0:
                    mem[j] = min(mem[j], mem[j - coin] + 1)
                
        return -1 if mem[-1] > amount else mem[-1]
    
#这道题只用建立一个一维数组就可以解决，而不用建二维数组，建二维数组不仅费内存，而且利用coin值不方便，直接用coins数组遍历就可以了
