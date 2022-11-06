def func_no1():
    while True:
        try:
            month=int(input())
            n=month-1

            def func(n):
                if n<2:  # 基线条件
                    return 1
                else:  # 递归条件
                    return func(n-1)+func(n-2)
            print(func(n))
        except:
            break


def my_func():
    n = int(input())
    dp = [[0] * 3 for _ in range(2)]
    dp[0][0] = 1
    for i in range(1,n):
        dp[i%2][0] = dp[(i-1)%2][1] + dp[(i-1)%2][2]
        dp[i%2][1] = dp[(i-1)%2][0] 
        dp[i%2][2] = dp[(i-1)%2][1] + dp[(i-1)%2][2]
    print(sum(dp[(n-1)%2]))


if __name__ == '__main__':
    # func_no1()
    my_func()