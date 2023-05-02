# $bo*y gi!r#l
s = input()
w = ''
l = []
for i in s:
    if i.isalpha():
        w += i
    elif w:
        l.append(w)
        w = ''
        
l.append(w)
for i in l[::-1]:
    print(i, end=' ')
        
