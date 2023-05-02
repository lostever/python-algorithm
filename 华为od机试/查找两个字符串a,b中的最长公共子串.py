# 排行第一名的代码
def no1_func():
    a = input()
    b = input()
    n = 0 
    s = ''
    if len(a) > len(b):
        a, b = b, a
    for i in range(len(a)+1):
        if a[i-n:i] in b:
            s = a[i-n:i]
            n += 1
    print(s)



# 我的代码
def my_func():
    # a = input()
    # b = input()
    a = 'abcdefghijklmnop'
    b = 'abcsafjklmnopqrstuvw'
    al = []
    bl = []
    for i in range(len(a)):
        for j in range(i+1,len(a)+1): #这里注意,外圈为起始索引,内圈为结束索引
            al.append(a[i:j])         #起始索引在第一项的左下角,
    for i in range(len(b)):           #而结束索引在末项的右下角,应为末项索引加一
        for j in range(i+1,len(b)+1): #所以range结束点加一,以防漏掉字符串最后一项
            bl.append(b[i:j])

    if len(al) > len(bl):
        shortl = bl
        longl = al
    else:
        shortl = al
        longl = bl




    max_legnth = 0
    ls = ''
    for i in shortl:
        if i in longl and len(i) > max_legnth:
            max_legnth = len(i)
            ls = i
    print(ls)

if __name__ == '__main__':
    
    my_func()
    # no1_func()

'''
描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！

数据范围：字符串长度1\le length \le300 \1≤length≤300 
进阶：时间复杂度：O(n^3)\O(n 
3
 ) ，空间复杂度：O(n)\O(n) 
输入描述：
输入两个字符串

输出描述：
返回重复出现的字符
示例1
输入：
abcdefghijklmnop
abcsafjklmnopqrstuvw
复制
输出：
jklmnop
'''