s = input()
f = ''
d = dict()
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
l = list(d.items())
for i in range(len(l)):
    for j in range(i+1, len(l)): # 注意此处range从i+1开始而不是从1开始
        if l[i][1] < l[j][1]:
            l[i], l[j] = l[j], l[i]
        elif l[i][1] == l[j][1] and ord(l[i][0]) > ord(l[j][0]):
            l[i], l[j] = l[j], l[i]
for i in l:
    print(i[0], end='')

'''
描述
输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出。
数据范围：字符串长度满足 1 \le len(str) \le 1000 \1≤len(str)≤1000 

输入描述：
一个只包含小写英文字母和数字的字符串。

输出描述：
一个字符串，为不同字母出现次数的降序表示。若出现次数相同，则按ASCII码的升序输出。

示例1
输入：
aaddccdc
复制
输出：
cda
复制
说明：
样例里，c和d出现3次，a出现2次，但c的ASCII码比d小，所以先输出c，再输出d，最后输出a.
     
'''
