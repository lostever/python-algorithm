def func(n):
    global d
    if d.get(n):
        return d[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    d[n] = func(n-1) + func(n-2)
    return d[n]

d = {}   
res = func(983)
print(res)