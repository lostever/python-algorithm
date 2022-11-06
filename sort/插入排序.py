def insert_sort(alist):
    n = len(alist)
    for i in range(1, n): # 将左边看成一个有序数组,将右边看成一个无序数组
        for j in range(i, 0, -1): # 排序的过程就是将无序数组的元素
            if alist[j] < alist[j-1]: # 一个个有序地加入有序数组
                alist[j], alist[j-1] = alist[j-1], alist[j]
            else:
                break

            
if __name__ == '__main__':
    a = [5,7,9,8,6,4,1,3,8,9,2,0,78,39,23,14,3,6]
    insert_sort(a)
    print(a)