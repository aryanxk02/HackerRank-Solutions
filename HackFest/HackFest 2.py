t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    y = []
    [y.append(x) for x in set(arr)]
    if arr == y:
        print('First')
    else:
        [arr.remove(i) for i in arr if arr.count(i) > 1]
        if (len(arr)+1) % 2 == 0:
            print('Second')
        else:
            print('First')