n_a, n_b = input().split()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = []
for i in range(max(a), min(b)+1):
    count1 = 0
    for num in a:
        if i%num == 0:
            count1 += 1
            if count1 == len(a):
                l.append(num)
print('l =', l)
x = []

for num in (l):
    count2 = 0
    for i in b:
        if i%num == 0:
            count2 += 1
            if count2 == len(b):
                x.append(num)
print('x =', x)
print(len(set(x)))