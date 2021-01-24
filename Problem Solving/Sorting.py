import time
start_time = time.time()

l =  list(map(int, input().split()))

# 2 5 4 7 6
# 2 4 4 6 7
for j in range(len(l)):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i+1], l[i] = l[i], l[i+1]
        else:
            pass
print(l)
print('Time : ', (time.time() - start_time))