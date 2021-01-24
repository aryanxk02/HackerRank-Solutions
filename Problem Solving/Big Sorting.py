import time
start_time = time.time()

n = int(input())
l = []
lnew = []
for i in range(n):
    l.append(int(input()))
for i in range(len(l)):
    lnew.append(min(l))
    l.remove(min(l))
for i in lnew:
    print(i)

print(time.time() - start_time)

# import time
# start_time = time.time()
#
# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))
# l.sort()
# for i in l:
#     print(i)
# print(time.time() - start_time)
#
