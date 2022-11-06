def func():
    n = int(input())
    s = 0
    while n > 1:
        l = '0'
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i != 1 and int(n/i) != i:
                    l += f'+{str(i)}+{str(int(n/i))}'
                else:
                    l += f'+{str(i)}'
        if eval(l) == n:
            s += 1
        n -= 1
    print(s)


def new_func():
    n = int(input())
    s = 0
    while n > 2:
        l = '1'
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                if int(n/i) != i:
                    l += f'+{str(i)}+{str(int(n/i))}'
                else:
                    l += f'+{str(i)}'
        if eval(l) == n:
            s += 1
        n -= 1
    print(s)


if __name__ == '__main__':
    
    new_func()

'''
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。

它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。

例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。

输入n，请输出n以内(含n)完全数的个数。

数据范围： 1 \le n \le 5 \times 10^{5} \1≤n≤5×10 
5
  
输入描述：
输入一个数字n

输出描述：
输出不超过n的完全数的个数

示例1
输入：
1000
复制
输出：
3
'''