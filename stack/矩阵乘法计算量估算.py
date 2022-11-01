n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
s = []
x = 0
for i in input():
    if i.isalpha():
        s.append(str(x))
        x += 1
    else:
        s.append(i)

# 此处将列表看作一个栈,如果遇到右括号,则将栈最顶两个矩阵相乘,
# 再将新得到的矩阵压入栈中,准备之后再次运算
stack = []
res = 0
for i in s:
    if i.isdigit():
        stack.append(l[int(i)])
    elif i == ')':
        b = stack.pop()
        a = stack.pop()
        res += a[0]*a[1]*b[1]
        stack.append([a[0],b[1]])
print(res)







        