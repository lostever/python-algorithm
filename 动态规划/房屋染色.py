# https://leetcode.cn/problems/JEj789/submissions/

class Solution:
    def minCost(self, costs) -> int:
        n = len(costs)
        dp = [[0]*3 for _ in range(n)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        i = 1
        while i<n:
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
            i += 1

        return min(dp[n-1])

# 滚动数组版本
class Solution1:
    def minCost(self, costs) -> int:
        n = len(costs)
        dp = [[0]*3 for _ in range(n)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        i = 1
        now, old = 0, 1
        while i<n:
            now, old = 1-now, now
            dp[now][0] = min(dp[old][1], dp[old][2]) + costs[i][0]
            dp[now][1] = min(dp[old][0], dp[old][2]) + costs[i][1]
            dp[now][2] = min(dp[old][0], dp[old][1]) + costs[i][2]
            i += 1

        return min(dp[now])

if __name__ == '__main__':
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    print(Solution1().minCost(costs))