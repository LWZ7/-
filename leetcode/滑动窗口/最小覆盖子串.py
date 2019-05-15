'''
给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        left = 0
        hashmap = {}
        minlen = 999999
        cnt = 0
        rs = ""
        # 建立t的hashmap
        for char in t:
            hashmap[char] = hashmap.get(char, 0) + 1
        # 遍历s
        for i in range(m):
            if(s[i] in hashmap.keys()):
                if(hashmap[s[i]]>0):
                    #计数已经出现的t的字符数
                    cnt += 1
                # hashmap -1
                hashmap[s[i]] -= 1
            # 知道了包含t的子串s[left: i+1]，进行左边扩增
            while(cnt == n):
                # 判断长度是否小于最小值，并更新
                if(i-left+1 < minlen):
                    minlen = i-left+1
                    rs = s[left:i+1]
                # 判断字符是否包含t的必要字符
                if(s[left] in hashmap.keys()):
                    # 判断cnt是否减少
                    if(hashmap[s[left]]+1>0):
                        cnt -= 1
                    # hashmap + 1
                    hashmap[s[left]] += 1
                # left右移1位
                left += 1
        return rs
