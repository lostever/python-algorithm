# https://www.nowcoder.com/practice/196534628ca6490ebce2e336b47b3607?tpId=37&tags=&title=&difficulty=2&judgeStatus=0&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D1%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37
a = int(input())
b = []
for c in range(2, int(a**0.5)+1):
    while a % c == 0:
        print(c,end=' ')
        a /= c
if a > 1:
    print(int(a))