def maxim(a, b, c):
    if a>b and a>c:
        print('Maximum :', a)
    elif b>a and b>c:
        print('Maximum :', b)
    else:
        print('Maximum :', c)
a = int(input())
b = int(input())
c = int(input())
maxim(a, b, c)
