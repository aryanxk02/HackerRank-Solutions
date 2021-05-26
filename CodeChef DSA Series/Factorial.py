def findTrailingZeros(n):
    count = 0
    i = 5
    while n / i >= 1:
        count += int(n / i)
        i *= 5
    return int(count)

t = int(input())
for _ in range(t):
    n = int(input())
    print(findTrailingZeros(n))
