n = int(input())
l1 = []
l2 = []
for _ in range(n):
    name = input()
    score = float(input())
    l1.append(name)
    l2.append(score)
    # print(l1)
    # print(l2)
l = [l2.index(min(l2))]
for i in range(0, len(l2), 1):
    print(i)
    if l2[i]==min(l2):
        l.append(l2.index(l2[i]))
print(l)
for i in range(len(l)):
    print(l1[i])