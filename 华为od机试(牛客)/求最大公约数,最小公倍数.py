# 辗转相除法求最大公约数
def gcd(x, y):
    if min(x,y) == 0:
        return max(x,y)
    return gcd(min(x,y), max(x,y)%min(x,y))


# 最小公倍数为 两数乘积除以最大公约数
def lcm(x, y):
    n = gcd(x,y)
    return int(x*y/n)


a, b = 369412, 289424
print(gcd(a, b))
print(lcm(a, b))
