n = int(input())
for _ in range(n):
    ct = 0
    a = input()
    ord_a = [ord(i) for i in a]
    rev_ord_a = ord_a[::-1]
    # print(ord_a)
    # print(rev_ord_a)
    l = []
    l2 = []
    for i in range(len(ord_a)-1):
        l.append(abs(ord_a[i+1]-ord_a[i]))
        l2.append(abs(rev_ord_a[i+1]-rev_ord_a[i]))
    # print(l)
    # print(l2)
    if l == l2:
        print('Funny')
    else:
        print('Not Funny')