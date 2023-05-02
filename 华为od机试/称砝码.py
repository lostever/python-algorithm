# 此题巧妙运用集合以及set()函数的特性.

N = int(input())
m = list(map(int,input().split()))
n = list(map(int,input().split()))
res = [0]
for i in range(N):
    s = [m[i] * j for j in range(n[i] + 1)]
    res = list(set(x+y for x in s for y in res))
print(len(res))

'''
描述
现有n种砝码，重量互不相等，分别为 m1,m2,m3…mn ；
每种砝码对应的数量为 x1,x2,x3...xn 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。


注：

称重重量包括 0

数据范围：每组输入数据满足 1 \le n \le 10 \1≤n≤10  ， 1 \le m_i \le 2000 \1≤m 
i
​
 ≤2000  ， 1 \le x_i \le 10 \1≤x 
i
​
 ≤10 
输入描述：
对于每组测试数据：
第一行：n --- 砝码的种数(范围[1,10])
第二行：m1 m2 m3 ... mn --- 每种砝码的重量(范围[1,2000])
第三行：x1 x2 x3 .... xn --- 每种砝码对应的数量(范围[1,10])
输出描述：
利用给定的砝码可以称出的不同的重量数

示例1
输入：
2
1 2
2 1
复制
输出：
5
复制
说明：
可以表示出0，1，2，3，4五种重量。   
'''