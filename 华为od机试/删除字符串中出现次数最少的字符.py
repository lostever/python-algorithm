# https://www.nowcoder.com/practice/05182d328eb848dda7fdd5e029a56da9?tpId=37&tags=&title=&difficulty=2&judgeStatus=0&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D1%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37
s = input()
if not s: 
    print(s)
else:
    s = list(s)
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    l = list(d.items())
    l.sort(key=lambda x:x[1])
    c = l[0][1]
    while l[0][1] == c:
        while l[0][0] in s:
            s.remove(l[0][0])
        l.pop(0)
    print(''.join(s))

