def extralongfactorials(n):
    fact = 1

    for i in range(n, 1, -1):
        fact = fact * i

    print(fact)

n = int(input())
extralongfactorials(n)