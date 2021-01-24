alice = list(map(int,input().split()))
bob = list(map(int,input().split()))
a, b = 0, 0
for i in range(0, len(alice)):
    if alice[i]>bob[i]:
        a += 1
    elif alice[i] == bob[i]:
        pass
    else:
        b += 1
print(a, b)


