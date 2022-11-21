l = [int(x) for x in list(input())]
s = set()
for i in range(len(l)-1, -1, -1):
    if l[i] not in s:
        print(l[i],end='')
        s.add(l[i])

'''
输入一个整数,将其倒排并去重
'''