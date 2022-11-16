# 插入排序

def insert_sort(l:list):
    for j in range(1,len(l)):
        for i in range(j, 0, -1):
            if l[i] < l[i-1]:
                l[i], l[i-1] = l[i-1], l[i]
            else:
                break
            
if __name__ == '__main__':
    l = [91, 22, 134, 214, 45, 625, 714, 8, 972]
    insert_sort(l)
    print(l)