def mult(l):
    for i in range(n):
        l.append(int(input()))
    total = 1
    for i in l:
        total = total * i
    print('Product :', total)
n = int(input())
l = []
mult(l)