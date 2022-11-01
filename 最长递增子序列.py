# 合唱队问题的子问题
def lis(list):
    dp = [1] * len(list)
    for i in range(len(list)):
        for j in range(i):
            if list[j] < list[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

list = [1,6,5,4,6,2,3,1]
print(lis(list))