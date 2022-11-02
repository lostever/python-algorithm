def bubble_sort(alist):
    # 冒泡排序
    n = len(alist)
    for i in range(n-1, 0, -1): # 外层循环控制比较轮数
        std = False  
        for j in range(i): # 内层循环控制每轮的比较数
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                std = True
        if not std: # 如果某一轮下来没有发生数据的位置交换
            break

if __name__ == '__main__':
    a = [1,3,8,9,5,7,9,8,6,4,2,0,23,14,3,6]
    bubble_sort(a)
    print(a)
    