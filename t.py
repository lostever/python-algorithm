## 合唱队问题

import bisect
def inc_max(l):
    dp = [1]*len(l) # 初始化dp，最小递增子序列长度为1
    arr = [l[0]] # 创建数组
    for i in range(1,len(l)): # 从原序列第二个元素开始遍历
        if l[i] > arr[-1]:
            arr.append(l[i])
            dp[i] = len(arr)
        else:
            pos = bisect.bisect_left(arr, l[i]) # 用二分法找到arr中第一个比ele_i大（或相等）的元素的位置
            arr[pos] = l[i]
            dp[i] = pos+1
    return dp
 
while True:
    try:
        N = int(input())
        s = list(map(int, input().split()))
        left_s = inc_max(s) # 从左至右
        right_s = inc_max(s[::-1])[::-1] # 从右至左
        sum_s = [left_s[i]+right_s[i]-1 for i in range(len(s))] # 相加并减去重复计算
        print(str(N-max(sum_s)))
    except:
        break