b = bin(int(input()))[2:]
a = b.split('0')
m = 0
for i in a:
    m = max(m, len(i))
print(m)