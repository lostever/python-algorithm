def insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
            else:
                break
if __name__ == '__main__':
    a = [5,7,9,8,6,4,1,3,8,9,2,0,78,39,23,14,3,6]
    insert_sort(a)
    print(a)