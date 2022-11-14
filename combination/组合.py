def comb1(k, available, used):
    if len(used) == k:
        yield used
    elif len(available) == 0:
        pass
    else:
        head = available.pop(0)
        used.append(head)
        for c in comb1(k, available[:], used[:]):
            yield c
        used.pop()
        for c in comb1(k, available[:], used[:]):
            yield c 

if __name__ == '__main__':
    n = 4
    k = 2
    for res in comb1(k,list(range(1,n+1)),[]):
        print(res)