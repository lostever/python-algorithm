def passjudge(s):
    if len(s) < 8:
        print('NG')
        return
    u,l,d,o = 0, 0, 0, 0
    if any(x.isupper() for x in s):
        u = 1
    if any(x.islower() for x in s):
        l = 1
    if any(x.isdigit() for x in s):
        d = 1
    if not s.isalnum():
        o = 1
    if u+l+d+o < 3:
        print('NG')
        return
    lst = []
    for i in range(len(s)-2):
        lst.append(s[i:i+3])
    set_lst = set(lst)
    if len(set_lst) != len(lst):
        print('NG')
        return
    print('OK')

while True:
    try:
        s = input()
        passjudge(s)
    except:
        break

'''
描述
密码要求:

1.长度超过8位

2.包括大小写字母.数字.其它符号,以上四种至少三种

3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）

数据范围：输入的字符串长度满足 1 \le n \le 100 \1≤n≤100 


输入：
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
复制
输出：
OK
NG
NG
OK
复制

'''