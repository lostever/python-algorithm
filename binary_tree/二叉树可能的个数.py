cache = {0: 1}

def count(x):
    w = cache.get(x, 0)
    if w:
        return w
    for k in range(x):
        w += count(k) * count(x - 1 -k)
    cache[x] = w
    return w

# print(len(str(count(186))))
print(count(int(input())))
