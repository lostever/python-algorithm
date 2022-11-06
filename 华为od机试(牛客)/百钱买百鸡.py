# for i in range(21):
#     for j in range(34):
#         for k in range(0, 301, 3):
#             if i + j + k == 100 and i*5 + j*3 + k/3 == 100:
#                 print(i, j, k)
                
# # 方法二
# for x in range(21):
#     for y in range(34):
#         z = 100 - y - x
#         if z % 3 == 0 and 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡：', x, '只', '母鸡：', y, '只', '小鸡：', z, '只')
            
while True:
    n = input()
    try:
        for i in range(21):
            for j in range(34):
                k = 100 - i - j 
                if k % 3 == 0 and i*5+j*3+int(k/3) == 100:
                    print(i, j, k)
    except:
        break