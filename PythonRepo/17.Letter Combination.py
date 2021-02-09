# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#
#
#  示例 1：
#
#
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
#  示例 2：
#
#
# 输入：digits = ""
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：digits = "2"
# 输出：["a","b","c"]
#
#
#
#
#  提示：
#
#
#  0 <= digits.length <= 4
#  digits[i] 是范围 ['2', '9'] 的一个数字。
#
#  Related Topics 深度优先搜索 递归 字符串 回溯算法
#  👍 1122 👎 0

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if not digits: return []

        digit_map = {
                 '2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}

        def combine(firstdigit, restdigit):

            if len(restdigit) == 0:
                result.append(firstdigit)
            else:
                for letter in digit_map[restdigit[0]]:
                    combine(firstdigit + letter, restdigit[1:])

        combine('',digits)

        return result