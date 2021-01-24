t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    m = []
    for i in range(len(l) + 1):
        [m.append(l[i:j]) for j in range(i + 1, len(l) + 1)]
    final = []
    for i in l:
        count = 0
        for j in m:
            if i == min(j):
                count += 1
        final.append(count)

    print(*final)
