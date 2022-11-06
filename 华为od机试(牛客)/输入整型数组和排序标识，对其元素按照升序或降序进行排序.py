# https://www.nowcoder.com/practice/dd0c6b26c9e541f5b935047ff4156309?tpId=37&tags=&title=&difficulty=1&judgeStatus=0&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D1%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37
n = int(input())
l = [int(x) for x in input().split()]
method = int(input())
def ins(alist, n):
    for i in range(n-1, 0, -1):
        std = False
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                std = True
        if not std:
            break

def des(alist, n):
    for i in range(n-1, 0, -1):
        std = False
        for j in range(i):
            if alist[j] < alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                std = True
        if not std:
            break
if method == 0:
    ins(l, n)
else:
    des(l, n)
print(*l,sep=' ')        
        
        