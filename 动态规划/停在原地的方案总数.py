# https://leetcode.cn/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if steps <= 1 or arrLen <= 1:
            return 1
        n = min(steps//2+1, arrLen)
        dp = [[0]*n for _ in range(steps+1)]
        dp[0][0] = 1
        for i in range(1, steps+1):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][n-1] = dp[i-1][n-2] + dp[i-1][n-1]
            for j in range(1, n-1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
        return dp[steps][0] % (10**9+7)

# 滚动数组优化版
class Solution1:
    def numWays(self, steps: int, arrLen: int) -> int:
        if steps <= 1 or arrLen <= 1:
            return 1
        n = min(steps//2+1, arrLen)
        dp = [[0]*n for _ in range(2)]
        dp[0][0] = 1
        now, pre = 0, 1
        for i in range(1, steps+1):
            pre, now = now, 1-now
            dp[now][0] = dp[pre][0] + dp[pre][1]
            dp[now][n-1] = dp[pre][n-2] + dp[pre][n-1]
            for j in range(1, n-1):
                dp[now][j] = dp[pre][j-1] + dp[pre][j] + dp[pre][j+1]
        return dp[steps&1][0] % (10**9+7)

if __name__ == '__main__':
    print(Solution1().numWays(500, 200))