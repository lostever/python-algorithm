def select_sort(alist):
    n = len(alist)
    for i in range(n-1):
        for j in range(i+1, n):
            if alist[j] < alist[i]:
                alist[i], alist[j] = alist[j], alist[i]
if __name__ == '__main__':
    a = [5,7,9,8,6,4,1,3,8,9,2,0,78,39,23,14,3,6]
    select_sort(a)
    print(a)