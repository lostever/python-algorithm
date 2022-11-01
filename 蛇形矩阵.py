# 排行第一名的代码:
def func():
    while True:
        try:
            num = int(input())
            for i in range(num):
                res = []
                if i == 0:
                    res = [(x+2)*(x+1)//2 for x in range(num)]
                else:
                    res = [x - 1 for x in res[1:]]
                print(' '.join(map(str, res)))
        except:
            break

    
# index 0, 1, 2, 3
# line: 1, 1+2, 1+2+3, 1+2+3+4 (1+i)
# row: 1, 1+1, 1+1+2, 1+1+2+3 
# 我的代码
def new_func():
    n = int(input())
    l = []

    for i in range(n):
        j = i
        ll = []
        w = 1
        while(j > 0):
            w += j
            j -= 1
        for x in range(n-i):
            ll.append(w)
            v = 2 + i + x
            w += v
        l.append(ll)

    for i in l:
        s =' '.join(list(map(str,i)))
        print(s)

if __name__ == '__main__':
    
    # func()
    new_func()

'''
描述
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

例如，当输入5时，应该输出的三角形为：

1 3 6 10 15

2 5 9 14

4 8 13

7 12

11


输入描述：
输入正整数N（N不大于100）

输出描述：
输出一个N行的蛇形矩阵。

示例1
输入：
4
复制
输出：
1 3 6 10
2 5 9
4 8
7
'''