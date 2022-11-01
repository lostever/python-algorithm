# https://www.nowcoder.com/practice/f33f5adc55f444baa0e0ca87ad8a6aac?tpId=295&tags=&title=&difficulty=0&judgeStatus=0&rp=0&sourceUrl=%2Fexam%2Foj
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
''' 滑动窗口的题放在动态规划下面真的过分了,妥妥的超时
class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        max = 0
        place = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    if dp[i][j] > max:
                        max = dp[i][j]
                        place = i                    
                else:
                    dp[i][j] = 0

        # 开始往回查找
        return str1[place-max: place]
'''
# 滑动窗口解法
class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        ans = ''
        length = 0
        for i in range(len(str1)+1):
            if str1[i-length: i] in str2:
                ans = str1[i-length: i]
                length += 1
        return ans