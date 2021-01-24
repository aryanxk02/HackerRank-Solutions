def equalStacks(h1, h2, h3):
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)

    while True:
        if s1 == 0 or s2 == 0 or s3 == 0:
            return 0
        elif s1 == s2 == s3:
            return s3
        elif s1 >= s2 and s1 >= s3:
            s1 = s1 - h1[0]
            h1.remove(h1[0])
        elif s2 >= s1 and s2 >= s3:
            s2 = s2 - h2[0]
            h2.remove(h2[0])
        elif s3 >= s1 and s3 >= s2:
            s3 = s3 - h3[0]
            h3.remove(h3[0])

x = list(map(int, input().split()))
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))
h3 = list(map(int, input().split()))