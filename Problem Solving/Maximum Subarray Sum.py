from collections import deque

test_case = int(input())

for _ in range(test_case):
    l = list(map(int, input().split()))

    list1 = list(map(int, input().split()))
    s = deque()

    for i in range(l[0] + 1):
        for j in range(i + 1, l[0] + 1):
            # print(type(i))
            # print(type(j))
            sub = list1[i:j]
            s.append(sub)

    x = deque()
    for i in s:
        x.append(sum(i) % l[1])
    print(max(x))

