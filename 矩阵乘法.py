x = int(input())
y = int(input())
z = int(input())
s1, s2 = list(), list()

for _ in range(x):
    s1.append(list(map(int, input().split())))
for _ in range(y):
    s2.append(list(map(int, input().split())))
# z = sum(map(lambda a,b: a*b, s1[0], [s2[n][0] for n in range(y)]))
# print(z)

s3 = []
for i in range(x):
    s3.append([0]*z)
    
for i in range(x):
    for j in range(z):
        s3[i][j] = sum(map(lambda a,b: a*b, s1[i], [s2[n][j] for n in range(y)]))
for i in range(x):
    print(*s3[i])
    
