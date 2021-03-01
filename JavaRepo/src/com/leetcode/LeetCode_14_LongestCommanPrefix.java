package com.leetcode;

/*
* # 编写一个函数来查找字符串数组中的最长公共前缀。
#
#  如果不存在公共前缀，返回空字符串 ""。
#
#
#
#  示例 1：
#
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#
#
#  示例 2：
#
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
#
#  提示：
#
#
#  0 <= strs.length <= 200
#  0 <= strs[i].length <= 200
#  strs[i] 仅由小写英文字母组成
#
#  Related Topics 字符串
#  👍 1448 👎 0
* */

import org.junit.Test;

public class LeetCode_14_LongestCommanPrefix {

    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0) {
            return "";
        }
        String ans = strs[0];
        for(int i =1;i<strs.length;i++) {
            int j=0;
            for(;j<ans.length() && j < strs[i].length();j++) {
                if(ans.charAt(j) != strs[i].charAt(j)) {
                    break;
                }
            }
            ans = ans.substring(0, j);
            if(ans.equals("")) {
                return ans;
            }
        }
        return ans;
    }


    @Test
    public void test(){
        System.out.println("print".charAt(4));
    }
}
