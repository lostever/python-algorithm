def combination(n,c,com=1,limit=0,res=[]):
    for pos in range(limit,n):
        t = res + [pos]
        if len(set(t)) == len(t):
            if len(t) == c:
                yield [pos,]
            else:
                for result in combination(n,c,com,com*pos, res + [pos,]):
                    yield [pos,] + result

                            
if __name__ == '__main__':
    print("排列：")
    for res in combination(8,8,0):
        print(res)

    # print("组合：")
    # for res in combination(3,3):
    #     print(res)

    # for res in combination(3,2):
    #     print(res)