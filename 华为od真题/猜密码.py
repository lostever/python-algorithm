from itertools import combinations

l = input().split(',')
l.sort()
n = len(l)
k = int(input())
res = []
if n < k:
    print(None)
else:
    for i in range(k, n+1):
        for j in combinations(l, i):
            res.append(j)

res.sort()
for x in res:
    print(','.join(x))


        
