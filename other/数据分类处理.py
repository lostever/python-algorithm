# https://www.nowcoder.com/practice/9a763ed59c7243bd8ab706b2da52b7fd?tpId=37&tags=&title=&difficulty=&judgeStatus=&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D1%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&gioEnter=menu

l = input().split()
M = int(l.pop(0))
r = list(map(int,input().split()))
N = r.pop(0)
r = sorted(set(r))
r = list(map(str,r))
res = []
for i in r:
    row = []
    cnt = 0
    for index, j in enumerate(l):
        if i in j:
            row += [index, j]
            cnt += 1
    if cnt:
        row = [i, cnt] + row
        res += row[:]
res = [len(res)] + res
print(*res)