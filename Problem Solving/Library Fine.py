def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1>y2:
        print(10000)
    elif y2==y1 and m1>m2:
        print(500*(m1-m2))
    elif y2==y1 and m2==m1 and d1>d2:
        print(15*(d1-d2))
    else:
         print(0)
d1, m1, y1 = list(map(int, input().split()))
d1 = int(d1)
m1 = int(m1)
y1 = int(y1)
d2, m2, y2 = list(map(int, input().split()))
d2 = int(d2)
m2 = int(m2)
y2 = int(y2)
libraryFine(d1, m1, y1, d2, m2, y2)