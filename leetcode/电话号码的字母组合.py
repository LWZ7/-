'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''
class Solution:
    dict_number = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    results = []
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.results=[]
        lenght = len(digits)
        if lenght==0:
            return []
        self.getResult(digits, 0, [])
        return self.results
    
    def getResult(self, digits, index, result):
        if index==len(digits):
            self.results.append(''.join(result))
            return
        for i in range(len(self.dict_number[digits[index]])):
            result.append(self.dict_number[digits[index]][i])
            self.getResult(digits,index+1, result)
            result.pop(index)
