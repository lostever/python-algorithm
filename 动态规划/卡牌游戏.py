# https://www.lintcode.com/problem/1448/description
# 此题与"盈利计划"几乎一致,只不过求的是大于total_profit(不包含)且小于total_cost(不包含)的结果
# 计算时,只需要将结果理解为大于等于(total_profit+1)且小于等于(total_cost-1)的项的结果
def num_of_plan(n: int, total_profit: int, total_cost: int, a, b) -> int:
    dp = [
        [[0]*total_cost for _ in range(total_profit+2)]
        for _ in range(n+1)
    ]
    for i in range(total_cost):
        dp[0][0][i] = 1
    for i in range(1,n+1):
        for j in range(total_profit+2):
            m = max(j-a[i-1],0)
            for k in range(total_cost):
                if k >= b[i-1]:
                    dp[i][j][k] = (dp[i-1][m][k-b[i-1]] + dp[i-1][j][k]) % (10**9+7)
                else:
                    dp[i][j][k] = dp[i-1][j][k]
    return dp[-1][-1][-1]

if __name__ == '__main__':
    n = 3
    total_profit = 5
    total_cost = 10
    a = [6,7,8]
    b = [2,3,5]
    # 输入：n = 3，totalProfit = 5，totalCost = 10，a = [6,7,8]，b = [2,3,5]
    print(num_of_plan(n, total_profit, total_cost, a, b ))