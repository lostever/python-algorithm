
# 运用队列和动态规划的思想
def editdistance(s1, s2):
    topen = [(s1, s2, 0)]
    opened = set()
    while True:
        w1, w2, value = topen.pop(0)
        if (w1, w2) in opened:
            continue
        if w1 == w2:
            return value
        opened.add((w1, w2))
        while w1 and w2 and w1[0] == w2[0]:
            w1, w2 = w1[1:], w2[1:]
        value += 1
        topen += [(w1,w2[1:],value),
                  (w1[1:],w2,value),
                  (w1[1:],w2[1:],value)]
        
a = input()
b = input()
print(editdistance(a,b))

'''
描述
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。编辑距离的算法是首先由俄国科学家 Levenshtein 提出的，故又叫 Levenshtein Distance 。

例如：

字符串A: abcdefg

字符串B: abcdef

通过增加或是删掉字符 ”g” 的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。

要求：

给定任意两个字符串，写出一个算法计算它们的编辑距离。


数据范围：给定的字符串长度满足 1 \le len(str) \le 1000 \1≤len(str)≤1000 


输入描述：
每组用例一共2行，为输入的两个字符串

输出描述：
每组用例输出一行，代表字符串的距离

示例1
输入：
abcdefg
abcdef
复制
输出：
1

'''