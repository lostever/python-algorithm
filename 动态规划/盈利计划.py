# https://leetcode.cn/problems/profitable-schemes/submissions/
#原始解题版
class Solution:
    def profitableSchemes(self, n, minProfit, group, profit) -> int:
        s = len(group)
        MOD = 10**9+7
        dp = [
            [
                [0] * (n+1)
                for _ in range(minProfit+1)
            ]   for _ in range(s+1)
        ]
        dp[0][0][0] = 1
        for i in range(1, s+1):
            for j in range(minProfit+1):
                for k in range(n+1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if k >= group[i-1]:
                        m = max(j-profit[i-1], 0)
                        dp[i][j][k] = (dp[i][j][k] + dp[i-1][m][k-group[i-1]]) % MOD
        return sum(dp[s][minProfit]) % MOD

#滚动数组版:
class Solution1:
    def profitableSchemes(self, n, minProfit, group, profit) -> int:
        s = len(group)
        MOD = 10**9+7
        dp = [
            [
                [0] * (n+1)
                for _ in range(minProfit+1)
            ]   for _ in range(2)
        ]
        for x in range(n+1):
            dp[0][0][x] = 1
        for i in range(1, s+1):
            for j in range(minProfit+1):
                for k in range(n+1):
                    dp[i%2][j][k] = dp[(i-1)%2][j][k]
                    if k >= group[i-1]:
                        m = max(j-profit[i-1], 0)
                        dp[i%2][j][k] = (dp[i%2][j][k] + dp[(i-1)%2][m][k-group[i-1]]) % MOD
        return dp[s%2][minProfit][n] % MOD
   
#二维数组1:
class Solution2:
    def profitableSchemes(self, n, minProfit, group, profit) -> int:
        s = len(group)
        MOD = 1000000007
        dp =[[0]*(n+1)for _ in range(minProfit+1)]
        for x in range(n+1):
            dp[0][x] = 1
        for i in range(s):
            tmp = [[0]*(n+1) for _ in range(minProfit+1)]
            for j in range(minProfit+1):
                m = max(j-profit[i], 0)
                for k in range(n+1):
                    tmp[j][k] = dp[j][k]
                    if k >= group[i]:
                        tmp[j][k] = (dp[m][k-group[i]] + tmp[j][k]) % MOD
            dp = tmp
        return dp[minProfit][n]
    
# 二维数组2:
class Solution3:
    def profitableSchemes(self, n, minProfit, group, profit) -> int:
        s = len(group)
        MOD = 1000000007
        dp = [[0]*(n+1)for _ in range(minProfit+1)]
        dp[0][0] = 1
        for i in range(s):
            tmp = [[0]*(n+1) for _ in range(minProfit+1)]
            for j in range(minProfit+1):
                m = max(j-profit[i], 0)
                for k in range(n+1):
                    tmp[j][k] = dp[j][k]
                    if k >= group[i]:
                        tmp[j][k] = (dp[m][k-group[i]] + tmp[j][k]) % MOD
            dp = tmp
        return sum(dp[minProfit]) % MOD
    
# 二维数组3:
class Solution4:
    def profitableSchemes(self, n, minProfit, group, profit) -> int:
        s = len(group)
        MOD = 1000000007
        dp = [[0]*(n+1)for _ in range(minProfit+1)]
        dp[0][0] = 1
        for i in range(s):
            for j in range(minProfit, -1, -1):
                m = max(j-profit[i], 0)
                for k in range(n, group[i]-1, -1):
                    dp[j][k] = (dp[m][k-group[i]] + dp[j][k]) % MOD
        return sum(dp[minProfit]) % MOD
        
if __name__ == '__main__':
    n = 25
    minProfit = 12
    group = [2,2,4,8,9]
    profit = [2,3,1,4,2]
    print(Solution4().profitableSchemes(n, minProfit, group, profit))