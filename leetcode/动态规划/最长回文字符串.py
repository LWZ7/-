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
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        k= len(s)
        matrix = [[0 for i in range(k)] for i in range(len(s))]
        logestSubStr = ""
        # 存储最长回文子串
        logestLen = 0
        # 最长回文子串的长度

        for j in range(0, len(s)):
            for i in range(0, j+1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        matrix[i][j] = 1
                        # 此时f(i,j)置为true
                        if logestLen < j - i + 1:
                            # 将s[i:j]的长度与当前的回文子串的最长长度相比 
                            logestSubStr = s[i:j+1]
                            # 取当前的最长回文子串
                            logestLen = j - i + 1
                            # 当前最长回文子串的长度
                else:
                    if s[i] == s[j] and matrix[i+1][j-1]:
                        # 判断
                        matrix[i][j] = 1
                        if logestLen < j - i + 1:
                            logestSubStr = s[i:j+1]
                            logestLen = j - i + 1
        return logestSubStr
