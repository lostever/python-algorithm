# https://www.nowcoder.com/practice/6d29638c85bb4ffd80c020fe244baf11?tpId=295&tags=&title=&difficulty=0&judgeStatus=0&rp=0&sourceUrl=
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , s1: str, s2: str) -> str:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        dir = [[0] * n for _ in range(m)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    dir[i-1][j-1] = 2 # 表明从左上角来(两字符相同)
                else:
                    if dp[i][j-1] > dp[i-1][j]:
                        dp[i][j] = dp[i][j-1]
                        dir[i-1][j-1] = 1 # 表明从左边来(两字符不同)
                    else:
                        dp[i][j] = dp[i-1][j]
                        dir[i-1][j-1] = 3 # 表明从上面来(两字符不同)
        # 开始根据dir还原选择的字符,如果输入的是s1,则使用i的位置,s2则用j
        ans = []
        def restore(i,j,s,dir,ans):
            if i < 0 or j < 0:
                return
            if dir[i][j] == 2:
                restore(i-1,j-1,s,dir,ans)
                ans.append(s[i])
            else:
                if dir[i][j] == 1:
                    restore(i,j-1,s,dir,ans)
                else:
                    restore(i-1,j,s,dir,ans)

        restore(m-1, n-1, s1, dir, ans)
        return ''.join(ans) if dp[-1][-1] else '-1'
    


        
