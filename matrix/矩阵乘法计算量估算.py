# https://www.nowcoder.com/practice/15e41630514445719a942e004edc0a5b?tpId=37&tags=&title=&difficulty=0&judgeStatus=&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D1%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&gioEnter=menu

n = int(input())
matrixs = []
for _ in range(n):
    matrixs.append([int(x) for x in input().split()])

exp = input()
stack = []
res = 0
for i in exp:
    if i == ')':
        b = stack.pop() # 这里一定要注意先后顺序,后面的是b, 前面的是a.
        a = stack.pop()
        res += a[0]*a[1]*b[1]
        stack.append([a[0], b[1]])
    elif i.isalpha():
        stack.append(matrixs.pop(0))

print(res)