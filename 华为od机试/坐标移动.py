import re 
pattern = re.compile('^[ADSW]\d{1,2}$')
s = input().split(';')
l = []
for i in s:
    ac = pattern.findall(i)
    if ac:
        l.append(ac[0])
x = y = 0
for i in l:
    if i[0] == 'A':
        x -= int(i[1:])
    elif i[0] == 'S':
        y -= int(i[1:])
    elif i[0] == 'W':
        y += int(i[1:])
    elif i[0] == 'D':
        x += int(i[1:])
print(f'{x},{y}')
    