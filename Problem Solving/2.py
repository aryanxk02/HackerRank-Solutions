def total_sum(l):
    total = 0
    for i in l:
        total = total + i
    print('Sum :', total)

n = int(input())
l = list(map(int, input().split()))
total_sum(l)