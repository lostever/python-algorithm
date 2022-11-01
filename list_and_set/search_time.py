import time
tl = time.time()
# l = [x for x in range(95536666)]
s = {x for x in range(95536666)}
print(time.time()-tl)
# ts = time.time()
# s = set(l)
# print(time.time()-ts)
# t1 = time.time()
# if 625366 in l:
#     print(True,time.time()-t1)
t2 = time.time()
if 62536676 in s:
    print(True,time.time()-t2)