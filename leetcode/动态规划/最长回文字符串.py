'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s :
            return ""
        res = ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        #print(dp)
        for i in range(n):
            #外循环顺向遍历,内循环逆向遍历
            for j in range(i,-1,-1):
                if s[i] == s[j] and (i - j < 2 or dp[i-1][j+1]):
                    #两个字符和一个字符直接判定，不用看前一个dp
                    dp[i][j] = 1
                if dp[i][j] and  max_len < i - j + 1:
                    #如果这是一个回文串，则判定它的长度
                    #print("i,j",i,j)
                    res = s[j:i+1]
                    max_len = i - j + 1
        return res 
